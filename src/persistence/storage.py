from typing import Annotated
from fastapi import Depends
from psycopg import AsyncConnection
from src.domain.contracts.IAnimal_Repository import IAnimalRepository
from src.domain.contracts.istorage import IStorage
from src.persistence.database import (build_conection)
from src.persistence.repositories.animal_repository import AnimalRepository


class __Storage(IStorage):
    
    #region repositories access 
    @property
    def animals(self)->IAnimalRepository:
        if self.__animalsRepository==None:
            self.__animalsRepository=AnimalRepository(self.__dbConn)
        return self.__animalsRepository

    #endregion
        
    def __init__(self,dbconnection:AsyncConnection):
        self.__dbConn=dbconnection

        #region repositoies instances
        self.__animalsRepository:AnimalRepository=None
        
        #endregion

        
    async def commit_async(self):
        self.__dbConn.commit()
        await self.__dbConn.transaction()

    async def rollback_async(self):
        self.__dbConn.rollback()
        self.__dbConn.transaction()

    def __del__(self):       
        if self.__dbConn:
            if self.__dbConn.closed:
                print('connection closed!')
                self.__dbConn.close()
            self.__dbConn=None
        #clean repositories instances
        self.__animalsRepository=None

        print("Repositories disposed!")