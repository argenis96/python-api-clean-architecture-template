from pydantic import BaseModel

class AnimalModel(BaseModel):
    id:int|None
    name:str|None
    category:str|None