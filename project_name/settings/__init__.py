import os
import importlib

ENV_ROLE = os.getenv('ENV_ROLE', 'development')

# change project_name to yours
env_settings = importlib.import_module(f'project_name.settings.{ENV_ROLE}') 

variables = vars(env_settings)

globals().update(variables)

try:
    from .local import *
except ImportError:
    pass
