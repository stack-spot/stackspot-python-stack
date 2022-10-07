from templateframework.metadata import Metadata
from os.path import isdir
from sys import exit


def run(metadata: Metadata = None):

    if isdir(__get_operation_id_folder_path(metadata)):
        print('Plugin has already been applied with this entries')

        exit(1)


def __get_operation_id_folder_path(metadata: Metadata):
    inputs_computed = metadata.computed_inputs
    target_path = metadata.target_path

    resource_folder_name = inputs_computed['resource_folder_name']
    operation_id_sanitized = inputs_computed['operation_id_sanitized']

    print(target_path / "src" / resource_folder_name  / operation_id_sanitized)
    return target_path / "src" / resource_folder_name  / operation_id_sanitized
