from abc import ABC,abstractmethod

from src.domain.entities.animal import Animal


class IAnimalRepository(ABC):

    @abstractmethod
    async def get_all_async(self)-> list[Animal]: 
        raise NotImplementedError

    @abstractmethod        
    async def get_by_id_async(self,id:int)-> Animal|None:  
       raise NotImplementedError

    @abstractmethod  
    async def update_async(self,animal:Animal):    
        raise NotImplementedError
    
    @abstractmethod  
    async def add_async(self,animal:Animal)->int:
        raise NotImplementedError

