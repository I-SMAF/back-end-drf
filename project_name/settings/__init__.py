import os
import importlib

ENV_ROLE = os.getenv('ENV_ROLE', 'development')

env_settings = importlib.import_module(f'back_end.settings.{ENV_ROLE}')

variables = vars(env_settings)

globals().update(variables)

try:
    from .local import *
except ImportError:
    pass
