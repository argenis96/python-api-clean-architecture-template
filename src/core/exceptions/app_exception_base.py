class AppExceptionBase(Exception):
    
    def __init__(self,message:str,messageCode:str,statusCode:int):
        self._message=message
        self._messageCode=messageCode
        self._statusCode=statusCode


     

