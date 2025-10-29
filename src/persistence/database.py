import psycopg
from src.shared.config import enviroment

config=enviroment.get_environment_settings()

async def build_conection()->psycopg.AsyncConnection:
    database_url=f"postgresql://{config.database.user}:{config.database.password}@{config.database.host}:{config.database.port}/{config.database.database_name}"
    return await psycopg.AsyncConnection.connect(database_url,autocommit=False)