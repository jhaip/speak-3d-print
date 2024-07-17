from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import requests
from pydub import AudioSegment
from openai import OpenAI
from dotenv import load_dotenv

import base64
import json
import tempfile
import time
from enum import Enum
from pathlib import Path
from urllib.request import Request, urlopen

import pythonlib.formlabs.formlabs as formlabs
import openapi_client
from openapi_client.models.auto_orient_post_request import AutoOrientPostRequest

app = Flask(__name__)
CORS(app)

# load environment variables from .env file
load_dotenv()
client = OpenAI()
KITTYCAD_API_TOKEN = os.environ['KITTYCAD_API_TOKEN']

def transcribe(audio_path):
    # Transcribe the audio using OpenAI Whisper
    with open(audio_path, 'rb') as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=f
        )
    return transcription.text


def call_zoo_api(prompt: str, output_format: str, output_dir: Path) -> Path | str:
    # https://zoo.dev/docs/api/ai/generate-a-cad-model-from-text
    # copied from https://github.com/KittyCAD/text-to-cad-blender-addon/blob/main/src/text_to_cad.py
    # define the url for the POST request
    post_url = f"https://api.zoo.dev/ai/text-to-cad/{output_format}"

    # define the authorization string
    auth = f"Bearer {KITTYCAD_API_TOKEN}"

    # create the json data string which contains our text prompt
    data = json.dumps({"prompt": prompt}).encode("utf-8")

    # define headers
    # the User-Agent header is necessary to prevent an HTTP 403 error
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }

    # create the response
    req = Request(post_url, data=data, headers=headers)

    with urlopen(req) as response:
        # decode the response to a dict
        result = json.loads(response.read().decode("utf-8"))

    # get the id of the request
    op_id = result["id"]

    # the requests are made asynchronously so keep checking the operations via the id
    # https://zoo.dev/docs/api/api-calls/get-an-async-operation
    while result["status"] not in ["completed", "failed"]:
        print("checking if the operation is completed")
        async_url = f"https://api.zoo.dev/async/operations/{op_id}"
        headers = {"Authorization": auth, "User-Agent": "Mozilla/5.0"}
        async_req = Request(async_url, headers=headers)
        with urlopen(async_req) as response:
            result = json.loads(response.read().decode("utf-8"))
        # using a sleep so that we don't keep pinging the site and get rate limited
        time.sleep(10)

    if result["status"] == "completed":
        # get the base64 encoded string of the output
        outputs = result["outputs"][f"source.{output_format}"]

        # this seems strange I have to do this. See the official kittycad implementation
        # https://github.com/KittyCAD/kittycad.py/blob/main/kittycad/models/base64data.py#L39
        decoded = base64.urlsafe_b64decode(outputs.strip("=") + "===")

        # save contents to a file on disk at the users location
        fp = output_dir / f"{op_id}.{output_format}"
        with open(fp, "wb") as out:
            out.write(decoded)

        return fp

    if result["status"] == "failed":
        # we've not generated an object for some reason
        # return the error string
        return result["error"]

def text_to_3d_model(prompt: str) -> Path | str:
    output_format = "stl"
    current_directory = Path.cwd()
    return call_zoo_api(prompt, output_format, current_directory)
    # mock by returning a locally saved .stl file
    # return Path("test.stl")

def convert_3d_model_to_printable_model(stl_file_path: Path) -> Path | str:
    print(f"Converting 3D model to printable model...")
    try:
        p = Path.home() / "code/build-PreForm-Desktop_Qt_5_15_2_clang_64bit-Debug/app/PreFormServer/output/PreFormServer.app/Contents/MacOS/PreFormServer"
        with formlabs.PreFormApi.start_preform_server(pathToPreformServer=p) as preform:
            print(f"Creating new scene...")
            preform.api.scene_post({
                "machine_type": "FRMB-3-0",
                "material_code": "FLGPBK04",
                "slice_thickness": 0.1,
                "print_setting": "LEGACY",
            })
            print(f"Importing model... {str(stl_file_path.resolve())}")
            # zoo.dev seems to produce models that are very small (unit scale)? so scale them up a bunch
            scale = 1000
            new_model = preform.api.scene_import_model_post({"file": str(stl_file_path.resolve()), "scale": scale})
            new_model_id = new_model.model_id
            print(f"Auto orienting...")
            preform.api.auto_orient_post(AutoOrientPostRequest.from_dict({"models": "ALL"}))
            print(f"Auto supporting...")
            preform.api.auto_support_post(AutoOrientPostRequest.from_dict({"models": "ALL"}))
            # print(f"Auto layout...")
            # preform.api.auto_layout_post_with_http_info(
            #     AutoOrientPostRequest.from_dict({"models": "ALL"})
            # )

            # TODO: probably replace .STL export with a thumbnail image
            print(f"Exporting model as .STL")
            exported_stl_path = Path("export.stl")
            preform.api.export_post(str(exported_stl_path))
            print(f"Exported STL file to {exported_stl_path}")

            exported_form_path = Path("export.form")
            preform.api.save_form_post(str(exported_form_path))
            print(f"Exported .form file to {exported_form_path}")
            return exported_stl_path
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/record', methods=['POST'])
def route_record():
    audio_file = request.files['audio']
    audio_path = "recording.wav"
    audio_file.save(audio_path)

    transcribed_text = transcribe(audio_path)
    print(f"Transcribed text: {transcribed_text}")
    return jsonify({"text":transcribed_text})

@app.route('/make-model', methods=['POST'])
def route_make_model():
    prompt = request.json['prompt']
    stl_file_path = text_to_3d_model(prompt)
    print(f"STL file path: {stl_file_path}")
    if isinstance(stl_file_path, str):
        return jsonify({"message": "Error", "error": stl_file_path})
    return jsonify({"message": "Model is ready", "file_path": stl_file_path.name})

@app.route('/make-printable-model', methods=['POST'])
def route_make_printable_model():
    stl_file_path = request.json['file_path']

    # using Preform API to do OCP and save the result as an .STL and a .form
    # return the path to the .stl and the .form
    result = convert_3d_model_to_printable_model(Path(stl_file_path))
    print(f"Printable model result: {result}")
    if isinstance(result, str):
        return jsonify({"message": "Error", "error": result})
    return jsonify({"message": "Printable model is ready", "file_path": result.name})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(port=8001, debug=True)
