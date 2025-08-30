
from fastapi import Depends
import psycopg
from src.persistence.database import (build_conection)
from src.domain.contracts.istorage import IStorage
from src.persistence.storage import __Storage
from src.core.services.animal_service import _AnimalService
from src.domain.contracts.ianimal_service import IAnimalService

def get_storage(conn:psycopg.AsyncConnection=Depends(build_conection)):
    return __Storage(conn)

def get_animal_service_dep(storage:IStorage=Depends(get_storage))->IAnimalService:  
    return _AnimalService(storage)