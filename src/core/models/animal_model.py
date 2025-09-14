from pydantic import BaseModel

class AnimalModel(BaseModel):
    id:int
    name:str
    category:str