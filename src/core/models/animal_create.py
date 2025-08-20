from pydantic import BaseModel

class AnimalCreate(BaseModel):
    name:str
    category:str
