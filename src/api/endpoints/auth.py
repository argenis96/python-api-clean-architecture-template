from typing import Annotated
from fastapi import APIRouter, Body

from src.core.models.auth_request_model import AuthRequestModel
from  ..auth import create_access_token


router=APIRouter(prefix="/api/v1/auth",tags=["auth"])

@router.post("/token",summary="generate access token")
def auth_token(credentials:Annotated[AuthRequestModel,Body()]):
    token=create_access_token({"username":"afeliz","email":"afeliz@com.do","roles":["pets.read","pets.add","pets.update"]})
    return {"access_token":token}