from abc import ABC,abstractmethod

from src.domain.contracts.IAnimal_Repository import IAnimalRepository

class IStorage(ABC):
        
    @property
    @abstractmethod
    def animals()->IAnimalRepository:
        raise NotImplementedError

    @abstractmethod
    async def commit_async(self):
        raise NotImplementedError
    
    @abstractmethod
    async def rollback_async(self):
         raise NotImplementedError