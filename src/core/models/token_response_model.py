import datetime
from pydantic import BaseModel

class TokenResponseModel(BaseModel):
    accessToken:str
    expireAt:datetime.datetime