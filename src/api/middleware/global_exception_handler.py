
from typing import List
from fastapi import Request,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.api.api_global_response import ApiGlobalResponse, Notification
from src.core.exceptions.app_exception_base import AppExceptionBase


def app_exception_handler(_: Request, ex: AppExceptionBase):
    return JSONResponse(status_code=ex._statusCode, content=ApiGlobalResponse[BaseModel](
        data=None,
        notifications=[
            Notification(message=ex._message, messageCode=ex._messageCode)
        ]
    ).model_dump(mode='python'))

def valitations_exception_handler(_: Request, ex: RequestValidationError):    
    ex.errors()
    notifications:List[Notification]=[]
    for error in ex.errors():
       field=error.get('loc', [])[1]
       message=error.get('msg')
       notifications.append(Notification(message=f'{field}: {message}',messageCode="10001"))     

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=ApiGlobalResponse[int](
                            data=None,
                            notifications=notifications
                        ).model_dump(mode='python'))

def exception_handler(_: Request, ex: Exception):
    #TODO Track exception to logs


    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=ApiGlobalResponse[BaseModel](
        data=None,
        notifications=[
            Notification(message="ocurrio un error interno mientras se procesaba su solicitud, favor intente mas tarde", messageCode=500)
        ]
    ).model_dump(mode='python'))