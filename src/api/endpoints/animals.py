

from fastapi import APIRouter, Body, Depends, Path
from fastapi.responses import JSONResponse
from src.api.api_global_response import ApiGlobalResponse
from src.api.middleware.global_api_route_handler import GlobalApiRouteHandler
from src.core.models.animal_model import AnimalModel
from src.core.models.animal_update import AnimalUpdate
from src.core.models.animal_create import AnimalCreate
from src.core.services.animal_service import AnimalService
from ..auth import check_access, verify_authentication


router=APIRouter(prefix="/api/v1/animals",tags=["animals"],route_class=GlobalApiRouteHandler,dependencies=[Depends(verify_authentication)])

@router.get("",summary="get all animals",dependencies=[Depends(check_access('pets.read'))],response_model=ApiGlobalResponse[list[AnimalModel]])
async def get_animals(animalService:AnimalService=Depends(AnimalService))->list[AnimalModel]:
    return await animalService.get_all_animals()

@router.get("/{id}",summary="get animal by id",dependencies=[Depends(check_access('pets.read'))],response_model=ApiGlobalResponse[AnimalModel])
async def get_animal_by_id(id:int=Path(),animalService:AnimalService=Depends(AnimalService))->AnimalModel:
    return await animalService.get_animal_by_id(id)

@router.post("",summary="add new animal",dependencies=[Depends(check_access('pets.read'))],response_model=ApiGlobalResponse[AnimalModel])
async def get_animals(data:AnimalCreate=Body(),animalService:AnimalService=Depends(AnimalService))->AnimalModel:
    return await animalService.add(data)


@router.put("/{id}",summary="update animal",dependencies=[Depends(check_access('pets.read'))],response_model=ApiGlobalResponse[AnimalModel])
async def get_animal_by_id(id:int=Path(),data:AnimalUpdate=Body(),animalService:AnimalService=Depends(AnimalService))->AnimalModel:
    return await animalService.update(id,data)

@router.delete("/{id}",summary="delete animal",dependencies=[Depends(check_access('pets.delete'))])
async def get_animal_by_id(id:int=Path(),animalService:AnimalService=Depends(AnimalService)):
    return JSONResponse(content=None,status_code=200)