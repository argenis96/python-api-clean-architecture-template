import json
import pickle
from typing import Any
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute

from src.api.api_global_response import ApiGlobalResponse


class GlobalApiRouteHandler(APIRoute):
    def get_route_handler(self):
        original_route_handler= super().get_route_handler()
        async def set_custom_responde_model(request:Request)->Response:
            try:
                response=await original_route_handler(request)
                if response.status_code>=200 and response.status_code<=400:
                    responseBody=json.loads(response.body.decode())
                    if responseBody:
                        bodyData=ApiGlobalResponse[Any](data=responseBody,notifications=[]).model_dump(mode='python')
                        return JSONResponse(content=bodyData,status_code=response.status_code)
                return response                    

            except Exception as e:
                raise e
        return set_custom_responde_model