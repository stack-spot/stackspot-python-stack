from re import finditer, search
from typing import List
from templateframework.metadata import Metadata

CHARACTER_QUERY_PARAM = '?'


def run(metadata: Metadata = None):
    inputs = metadata.all_inputs()
    inputs_local = metadata.inputs
    inputs_global = metadata.global_inputs
    inputs_computed_global = metadata.global_computed_inputs
    target_path = metadata.target_path
    component_path = metadata.component_path
    stack_path = metadata.stack_path

    uri = inputs['uri']
    method = inputs['method_sanitized']
    resource = inputs['resource']
    resource_folder_name = inputs['resource_folder_name']
    resource_response = inputs['resource_response']

    uri_contain_resource_id = __uri_contain_resource_id(uri)
    should_response_as_list = __should_response_as_list(uri_contain_resource_id, method)
    contain_resource_parameter = __should_contain_resource_parameter(method)

    metadata.computed_inputs['parameters'] = __get_parameters(uri, method, resource, resource_folder_name, contain_resource_parameter)
    metadata.computed_inputs['uri_contain_resource_id'] = uri_contain_resource_id
    metadata.computed_inputs['should_response_as_list'] = should_response_as_list
    metadata.computed_inputs['contain_resource_parameter'] = contain_resource_parameter
    metadata.computed_inputs['resource_response_full_sanitized'] = f'List[{resource_response}]' if should_response_as_list else resource_response

    return metadata


def __get_parameters(
        uri,
        method,
        resource_request,
        resource_folder_name,
        contain_resource_parameter) -> List[str]:
    uri_params_groups = finditer(r'\{(?P<parameter>([a-z]+(-[a-z]*)+)|[a-z]+)\}', uri)
    parameters = []

    if uri_params_groups:
        for uri_param_group in uri_params_groups:
            parameter = uri_param_group.group('parameter')
            parameter = parameter.replace('-', '_')
            parameters.append((parameter, 'str'))

    if __should_contain_resource_parameter(method):
        parameters.append((resource_folder_name, f'{resource_request}Request'))

    return parameters


def __should_response_as_list(
        uri_contain_resource_id: bool,
        method: str) -> bool:
    return not uri_contain_resource_id and method == 'get'


def __should_contain_resource_parameter(method: str) -> bool:
    return method in ['post', 'put', 'patch']


def __get_uri_without_query_parms(uri) -> str:
    return uri[:__get_query_param_index(uri)] if __contain_query_params(uri) != -1 else uri


def __contain_query_params(uri) -> bool:
    return uri.find(CHARACTER_QUERY_PARAM)


def __get_query_param_index(uri) -> int:
    return uri.index(CHARACTER_QUERY_PARAM)


def __uri_contain_resource_id(uri):
    uri_without_query_params = __get_uri_without_query_parms(uri)

    return search(r'(?P<resource_parameter>\/{[a-zA-Z]*(-[a-zA-Z]*)*}$)', uri_without_query_params) is not None

