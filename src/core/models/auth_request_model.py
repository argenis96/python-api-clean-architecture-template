from pydantic import BaseModel, Field


class AuthRequestModel(BaseModel):
    username:str=Field(max_length=20,min_length=5)
    password:str=Field(max_length=20,min_length=5)