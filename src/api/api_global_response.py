
from enum import Enum
from typing import Generic, TypeVar, Union
from pydantic import BaseModel

T = TypeVar('T',bound=BaseModel)
class MessageType(Enum):
   VALIDATION_ERROR="VALIDATION"

class Notification(BaseModel):
   message:str
   messageCode:int

class ApiGlobalResponse(BaseModel,Generic[T]):
   data:Union[T,None]
   notifications:Union[list[Notification],None]


