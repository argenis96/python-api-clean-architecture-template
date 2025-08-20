from fastapi import Depends
from psycopg import AsyncConnection
from src.persistence.database import (build_conection)
from src.persistence.repositories.animal_repository import AnimalRepository


class Storage:

    def __init__(self,dbconnection:AsyncConnection=Depends(build_conection)):
        self.__dbConn=dbconnection

        #Define repositories
        self.animals=AnimalRepository(self.__dbConn)

    async def commit_async(self):
        self.__dbConn.commit()
        await self.__dbConn.transaction()

    async def rollback_async(self):
        self.__dbConn.rollback()
        self.__dbConn.transaction()

        