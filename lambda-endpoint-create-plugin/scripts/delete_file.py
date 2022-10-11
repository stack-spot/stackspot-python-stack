from templateframework.metadata import Metadata
from os import remove
from os.path import exists


def run(metadata: Metadata = None):
    target_path = metadata.target_path
    inputs_computed = metadata.computed_inputs

    should_response_data = inputs_computed['should_response_data']

    if not should_response_data:
        resource_folder_name = inputs_computed['resource_folder_name']
        operation_id_sanitized = inputs_computed['operation_id_sanitized']
        path = target_path / "src" / resource_folder_name / operation_id_sanitized / "models.py"

        if exists(path):
            remove(path)