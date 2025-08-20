from fastapi import status
from src.core.exceptions.app_exception_base import AppExceptionBase

class AppOperationException(AppExceptionBase):
   def __init__(self, message:str,messageCode:str):
        super().__init__(message,messageCode,status.HTTP_500_INTERNAL_SERVER_ERROR)

class AppUnauthorizedException(AppExceptionBase):
    def __init__(self, message:str,messageCode:str):
        super().__init__(message,messageCode,status.HTTP_403_FORBIDDEN)

class AppAutenticationException(AppExceptionBase):
   def __init__(self, message:str,messageCode:str):
        super().__init__(message,messageCode,status.HTTP_401_UNAUTHORIZED)
        
class AppValidationException(AppExceptionBase):
   def __init__(self, message:str,messageCode:str):
        super().__init__(message,messageCode,status.HTTP_400_BAD_REQUEST)

class AppNotFoundException(AppExceptionBase):
   def __init__(self, message:str,messageCode:str):
        super().__init__(message,messageCode,status.HTTP_404_NOT_FOUND)