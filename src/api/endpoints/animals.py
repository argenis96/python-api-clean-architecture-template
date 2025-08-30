

from typing import Annotated
from fastapi import APIRouter, Body, Depends, Path
from fastapi.responses import JSONResponse
from src.domain.contracts.ianimal_service import IAnimalService
from src.api.middleware.global_api_route_handler import GlobalApiRouteHandler
from src.core.models.animal_model import AnimalModel
from src.core.models.animal_update import AnimalUpdate
from src.core.models.animal_create import AnimalCreate
from src.domain.contracts.ianimal_service import IAnimalService
from ..auth import check_access, verify_authentication
from src.core.dependencies import get_animal_service_dep


router=APIRouter(prefix="/api/v1/animals",tags=["animals"],route_class=GlobalApiRouteHandler,dependencies=[Depends(verify_authentication)])

@router.get("",summary="get all animals",dependencies=[Depends(check_access('pets.read'))])
async def get_animals(animalService:IAnimalService=Depends(get_animal_service_dep))->list[AnimalModel]:
    return await animalService.get_all_animals()

@router.get("/{id}",summary="get animal by id",dependencies=[Depends(check_access('pets.read'))])
async def get_animal_by_id(animalService:IAnimalService=Depends(get_animal_service_dep),id:int=Path())->AnimalModel:
    animal= await animalService.get_animal_by_id(id)
    return animal

@router.post("",summary="add new animal",dependencies=[Depends(check_access('pets.read'))])
async def get_animals(animalService:IAnimalService=Depends(get_animal_service_dep),data:AnimalCreate=Body())->AnimalModel:
    return await animalService.add(data)


@router.put("/{id}",summary="update animal",dependencies=[Depends(check_access('pets.read'))])
async def get_animal_by_id(animalService:IAnimalService=Depends(get_animal_service_dep),id:int=Path(),data:AnimalUpdate=Body())->AnimalModel:
    return await animalService.update(id,data)

@router.delete("/{id}",summary="delete animal",dependencies=[Depends(check_access('pets.delete'))])
async def get_animal_by_id(animalService:IAnimalService=Depends(get_animal_service_dep),id:int=Path()):
    return JSONResponse(content=None,status_code=200)