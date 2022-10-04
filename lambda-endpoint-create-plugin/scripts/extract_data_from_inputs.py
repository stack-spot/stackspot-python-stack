from re import finditer
from templateframework.metadata import Metadata

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


    metadata.global_computed_inputs['parameters'] = get_parameters(uri, method, resource, resource_folder_name)
    
    return metadata
    
def get_parameters(uri, method,  resource, resource_folder_name):
    uri_params_groups = finditer(r'\{(?P<parameter>([a-z]+(-[a-z]*)+)|[a-z]+)\}', uri)
    parameters = []

    if uri_params_groups:
        for uri_param_group in uri_params_groups:
            parameter = uri_param_group.group('parameter')
            parameter = parameter.replace('-', '_')
            parameters.append((parameter, 'str'))

    if __contain_resource_parameter(method):
        parameters.append((resource_folder_name, resource))

    return parameters
    

def __contain_resource_parameter(method: str):
    return method in ['post', 'put', 'patch']