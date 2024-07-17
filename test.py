from pathlib import Path
import pythonlib.formlabs.formlabs as formlabs
import openapi_client
from openapi_client.models.auto_orient_post_request import AutoOrientPostRequest

def convert_3d_model_to_printable_model(stl_file_path: Path) -> Path | str:
    print(f"Converting 3D model to printable model...")
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
        new_model = preform.api.scene_import_model_post({"file": str(stl_file_path.resolve())})
        new_model_id = new_model.model_id
        print(f"Auto orienting...")
        preform.api.auto_orient_post(AutoOrientPostRequest.from_dict({"models": "ALL"}))
        print(f"Auto supporting...")
        preform.api.auto_support_post(AutoOrientPostRequest.from_dict({"models": "ALL"}))
        print(f"Auto layout...")
        preform.api.auto_layout_post_with_http_info(
            AutoOrientPostRequest.from_dict({"models": "ALL"})
        )

        # TODO: probably replace .STL export with a thumbnail image
        print(f"Exporting model as .STL")
        exported_stl_path = Path("export.stl")
        preform.api.export_post(str(exported_stl_path))
        print(f"Exported STL file to {exported_stl_path}")

        exported_form_path = Path("export.form")
        preform.api.save_form_post(str(exported_form_path))
        print(f"Exported .form file to {exported_form_path}")
        return exported_stl_path

if __name__ == "__main__":
    convert_3d_model_to_printable_model(Path("test.stl"))