
from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource,JsonConfigSettingsSource



class DataBaseSettings(BaseSettings):
    host:str
    port:int
    user:str
    password:str
    database_name:str
class EnviromentSettings(BaseSettings):  
    app_name:str
    app_description:str
    app_version:str
    app_path_base:str
    database:Optional[DataBaseSettings]



    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (env_settings,JsonConfigSettingsSource(settings_cls,json_file="settings.json"))

@lru_cache
def get_environment_settings()->EnviromentSettings:
    return EnviromentSettings()