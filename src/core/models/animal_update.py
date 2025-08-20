from pydantic import BaseModel


class AnimalUpdate(BaseModel):
    name:str
    category:str