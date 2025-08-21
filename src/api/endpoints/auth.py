from typing import Annotated
from fastapi import APIRouter, Body

from src.api.api_global_response import ApiGlobalResponse
from src.api.middleware.global_api_route_handler import GlobalApiRouteHandler
from src.core.models.auth_request_model import AuthRequestModel
from src.core.models.token_response_model import TokenResponseModel
from  ..auth import create_access_token


router=APIRouter(prefix="/api/v1/auth",tags=["auth"],route_class=GlobalApiRouteHandler)

@router.post("/token",summary="generate access token")
def auth_token(credentials:Annotated[AuthRequestModel,Body()]):
    return create_access_token({"username":"afeliz","email":"afeliz@com.do","roles":["pets.read","pets.add","pets.update"]})