from re import finditer, search
from typing import List
from templateframework.metadata import Metadata
from random import randint

CHARACTER_QUERY_PARAM = '?'
REGEX_GET_PARAMETERS_OF_URI = r'\{(?P<parameter>[a-zA-Z]*(-[a-zA-Z]+)*?)\}'


def run(metadata: Metadata = None):
    inputs_local = metadata.inputs
    inputs_computed = metadata.computed_inputs

    uri = inputs_local['uri']
    method = inputs_computed['method_sanitized']
    resource_request = inputs_computed['resource_request']
    resource_folder_name = inputs_computed['resource_folder_name']
    resource_response = inputs_computed['resource_response']
    
    uri_sanitized = __get_uri_sanitized(uri)
    uri_sanitized_for_test = __generate_uri_sanitized_for_test(uri)
    uri_sanitized_without_query_parms = __get_uri_without_query_parms(uri_sanitized)
    uri_contain_resource_id = __uri_contain_resource_id(uri)
    should_response_as_list = __should_response_as_list(uri_contain_resource_id, method)
    contain_resource_parameter = __should_contain_resource_parameter(method)

    metadata.computed_inputs['parameters'] = __get_parameters(uri, resource_request, resource_folder_name, contain_resource_parameter)
    metadata.computed_inputs['uri_contain_resource_id'] = uri_contain_resource_id
    metadata.computed_inputs['should_response_as_list'] = should_response_as_list
    metadata.computed_inputs['contain_resource_parameter'] = contain_resource_parameter
    metadata.computed_inputs['uri_sanitized'] = uri_sanitized
    metadata.computed_inputs['uri_sanitized_for_test'] = uri_sanitized_for_test
    metadata.computed_inputs['uri_sanitized_without_query_parms'] = uri_sanitized_without_query_parms
    metadata.computed_inputs['resource_response_full_sanitized'] = f'List[{resource_response}]' if should_response_as_list else resource_response

    return metadata


def __get_parameters(
        uri,
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

    if contain_resource_parameter:
        parameters.append((resource_folder_name, resource_request))

    return parameters


def __get_uri_sanitized(uri: str) -> str:
    ocurrences = finditer(REGEX_GET_PARAMETERS_OF_URI, uri)
    for ocurrence in ocurrences:
        parameter_not_sanitized = ocurrence.group('parameter')
        parameter_sanitized = parameter_not_sanitized.replace('-', '_')
        uri = uri.replace(parameter_not_sanitized, parameter_sanitized)
    
    uri = uri.replace('amp;', '')

    return uri

def __generate_uri_sanitized_for_test(uri: str) -> str:
    ocurrences = finditer(REGEX_GET_PARAMETERS_OF_URI, uri)
    for ocurrence in ocurrences:
        parameter_not_sanitized = ocurrence.group('parameter')
        number_replacement = randint(1, 200)
        uri = uri.replace(f'{{{parameter_not_sanitized}}}', str(number_replacement))

    return uri
    
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

