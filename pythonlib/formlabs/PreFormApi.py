"""\
Handwritten convenience wrapper around the generated Python library code
"""
from contextlib import contextmanager
import formlabs
import subprocess
import os
import sys

class PreFormApi:
    server_process = None

    def __init__(self, preform_port=44388):
        self.preform_port = preform_port
        self.client = formlabs.ApiClient(
            formlabs.Configuration(host=f"http://localhost:{preform_port}")
        )
        self.api = formlabs.DefaultApi(self.client)

    @staticmethod
    def start_preform_sync(pathToPreformServer=None, preform_port=44388):
        preformserver_path = _find_preform_server(pathToPreformServer)

        server_process = subprocess.Popen(
            [preformserver_path, "--port", str(preform_port)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True)

        while True:
            output = server_process.stdout.readline()
            if output:
                if "READY FOR INPUT" in output:
                    preformApi = PreFormApi(preform_port)
                    preformApi.server_process = server_process
                    return preformApi
            elif server_process.poll() is not None:
                return_code = server_process.returncode
                if return_code != 0:
                    error_message = server_process.stderr.read()
                    raise RuntimeError(f"Server process terminated while starting with return code {return_code}: {error_message}")
                else:
                    raise RuntimeError("Server process terminated while starting.")

    # This solves a problem while developing where it's easy to end up with an orphaned server process
    # TODO: start_preform_server_if_needed
    @contextmanager
    @staticmethod
    def start_preform_server(pathToPreformServer=None, preform_port=44388):
        preformApi = None
        try:
            preformApi = PreFormApi.start_preform_sync(pathToPreformServer, preform_port)
            print("PreForm server ready")
            yield preformApi
            return
        finally:
            if (preformApi):
                preformApi.stop_preform_server()
                print("PreForm server stopped.")

    def stop_preform_server(self):
        if self.server_process is not None:
            self.server_process.terminate()
            self.server_process.wait()
            self.server_process = None

def _find_preform_server(pathToPreformServer=None):
    if pathToPreformServer is None:
        formlabs_path = os.path.dirname(os.path.realpath(__file__))
        library_path = os.path.dirname(os.path.dirname(formlabs_path))

        filename = "PreFormServer"
        if sys.platform == "win32":
            filename += ".exe"

        pathToPreformServer = os.path.join(library_path, filename)
    if not os.path.isfile(pathToPreformServer):
        raise FileNotFoundError("PreFormServer executable not found at " + pathToPreformServer)

    return pathToPreformServer

