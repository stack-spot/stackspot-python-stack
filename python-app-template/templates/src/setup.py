from setuptools import setup

setup(
    name='{{project_name_sanitized}}',
    version='{{project_version}}',
    description='{{inputs.project_description}}',
    packages=['{{project_name_sanitized}}'],  #same as name
    install_requires=['wheel', 'pytest'], #external packages as dependencies
)