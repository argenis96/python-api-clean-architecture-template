from functools import lru_cache
import psycopg

from src.shared.config import enviroment

config=enviroment.get_environment_settings()

async def build_conection()->psycopg.AsyncConnection:
    return await psycopg.AsyncConnection.connect(config.DATA_BASE_CONNECTION,autocommit=False)