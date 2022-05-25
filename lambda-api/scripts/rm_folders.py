import shutil
import os
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
  project_name_sanitized = metadata.all_inputs()["project_name_sanitized"]
  shutil.rmtree(f'{os.getcwd()}/src/{project_name_sanitized}')
  shutil.rmtree(f'{os.getcwd()}/src/tests')
