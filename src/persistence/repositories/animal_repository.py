
from psycopg import AsyncConnection
import pydapper
from src.domain.entities.animal import Animal
from src.persistence.repositories.raw_queries.animals_query import AnimalQuery

class AnimalRepository:
    def __init__(self,connection:AsyncConnection):
        self.__dbconnection=connection

    async def get_all_async(self)-> list[Animal]:   
        commands=pydapper.using_async(self.__dbconnection)
        return await commands.query_async(sql=AnimalQuery.GET_ALL_ANIMALS,model=Animal,)
        
    async def get_by_id_async(self,id:int)-> Animal|None:          
        commands=pydapper.using_async(self.__dbconnection)
        return await commands.query_first_or_default_async(sql=AnimalQuery.GET_ANIMAL_BY_ID,default=None,model=Animal,param={"AnimalId":id})
            
    async def update_async(self,animal:Animal):          
        commands=pydapper.using_async(self.__dbconnection)
        await commands.execute_async(sql=AnimalQuery.UPDATE_ANIMAL_BY_ID,param=animal.__dict__)
            
    async def add_async(self,animal:Animal)->int:
        commands=pydapper.using_async(self.__dbconnection)
        animal.id=0
        return await commands.execute_scalar_async(sql=AnimalQuery.INSERT,param=animal.__dict__)