
from typing import Union
from src.core.models.animal_create import AnimalCreate
from src.core.models.animal_model import AnimalModel
from src.core.models.animal_update import AnimalUpdate
from src.domain.contracts.istorage import IStorage
from src.domain.contracts.ianimal_service import IAnimalService
from src.domain.entities.animal import Animal
from src.core.exceptions.app_exceptions import AppNotFoundException

class _AnimalService(IAnimalService):
        def __init__(self,storage:IStorage):
                self.__db=storage
        
        async def get_all_animals(self)->Union[list[AnimalModel],None]:
                animals=await self.__db.animals.get_all_async()
                return [AnimalModel(**item.__dict__) for item in animals]
        
        async def get_animal_by_id(self,id:int)->Union[AnimalModel,None]:
                animal=await self.__db.animals.get_by_id_async(id)
                if not animal:
                  raise AppNotFoundException(message=f"no existe un animal registrado con el id '{id}'",messageCode="10007")
                
                return AnimalModel(**animal.__dict__)

        async def update(self,id:int,data:AnimalUpdate)->Union[AnimalModel,None]:
                ## TODO VALIDACIONES, SI EXISTE, SI SE PUEDE MODIFICAR ETC

                animal=Animal(id=id,name=data.name,category=data.category)
                await self.__db.animals.update_async(animal)
                await self.__db.commit_async()
                return AnimalModel(**animal.__dict__)
        
        async def add(self,data:AnimalCreate)->Union[int,None]:
                ## TODO VALIDACIONES, SI EXISTE, SI SE PUEDE MODIFICAR ETC
                #SI EXISTE PUEDES RETORNAR UN APP EXCEPTION EJEMPLO: raise AppOperationException(message=f"ya existe un animal registrado con el nombre '{data.name}'",messageCode="10007")                
                animal=Animal(id=id,name=data.name,category=data.category)
                animalId=await self.__db.animals.add_async(animal)
                animal.id=animalId

                await self.__db.commit_async()
                #await self.__db.rollback_async()
                return AnimalModel(**animal.__dict__)