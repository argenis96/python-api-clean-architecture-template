import datetime
from typing import Union
from pydantic import BaseModel

class TokenResponseModel(BaseModel):
    accessToken:Union[str,None]
    expireAt:Union[str,None]