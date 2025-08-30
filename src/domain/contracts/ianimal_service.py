from abc import ABC, abstractmethod
from typing import Union

from src.core.models.animal_create import AnimalCreate
from src.core.models.animal_model import AnimalModel
from src.core.models.animal_update import AnimalUpdate


class IAnimalService(ABC):
    @abstractmethod
    async def get_all_animals(self)->Union[list[AnimalModel],None]:
        pass
    
    @abstractmethod
    async def get_animal_by_id(self,id:int)->Union[AnimalModel,None]:
        pass
    
    @abstractmethod
    async def update(self,id:int,data:AnimalUpdate)->Union[AnimalModel,None]:
        pass
    
    @abstractmethod
    async def add(self,data:AnimalCreate)->Union[int,None]:
        pass