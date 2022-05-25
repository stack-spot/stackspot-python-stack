import shutil
import os
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
  shutil.move(f'{os.getcwd()}/src/pyproject.toml', f'{os.getcwd()}/pyproject.toml')
