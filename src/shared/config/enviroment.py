
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENVIROMENT")
    return f".env.{runtime_env}" if runtime_env else ".env"

class EnviromentSettings(BaseSettings):
    APP_NAME:str|None=""
    DATA_BASE_CONNECTION:str|None=""
    API_DESCRIPTION:str|None=""
    API_VERSION:str|None=""
    PATH_BASE:str|None=""

    model_config=SettingsConfigDict(env_file=get_env_filename()) 

@lru_cache
def get_environment_settings()->EnviromentSettings:
    return EnviromentSettings()