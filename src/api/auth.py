from typing import Annotated
from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security.http import  HTTPBearer
import jwt,datetime
from src.core.exceptions.app_exceptions import AppAutenticationException,AppUnauthorizedException
from src.core.models.token_response_model import TokenResponseModel

auth_schema=HTTPBearer(auto_error=False)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_authentication(authCredentials:Annotated[HTTPAuthorizationCredentials,Depends(auth_schema)])->dict:
    if not authCredentials:
        raise AppAutenticationException("You must be authenticated to perform this action.",messageCode="10005")
    return decode_token(token=authCredentials.credentials)

def decode_token(token:str)->dict:
    try:
        payload= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        raise  AppAutenticationException("session expired",messageCode="10005")
    except Exception as e:
        raise  AppAutenticationException("invalid token",messageCode="10005")

def create_access_token(payload:dict)->TokenResponseModel:
    to_encode = payload.copy()
    expire=datetime.datetime.utcnow()+datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)
    return TokenResponseModel(accessToken=encoded_jwt,expireAt=expire.strftime("%y-%m-%d %H:%M:%S"))

def get_current_user(claims:Annotated[dict,Depends(verify_authentication)])->dict:
    return {"username":claims.get("username"),"email":claims.get("email")}

def check_access(access:str):
    def role_check(claims:dict=Depends(verify_authentication)):
        roles=claims.get("roles",[])
        if access not in roles:
            raise  AppUnauthorizedException(message="you do not have permission to perform this action",messageCode="1005")
    return role_check