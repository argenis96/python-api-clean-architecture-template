from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from src.api.middleware.global_exception_handler import app_exception_handler, exception_handler, valitations_exception_handler
from src.core.exceptions.app_exception_base import AppExceptionBase
from src.shared.config import enviroment
from src.api.endpoints import animals, auth
config=enviroment.get_environment_settings()
app = FastAPI(
    docs_url='/',
    title=f"{config.APP_NAME}[{config.API_VERSION}]",
    description =f"{config.API_DESCRIPTION}",
    root_path=f"/{config.PATH_BASE}"
)
app.add_exception_handler(AppExceptionBase,app_exception_handler)
app.add_exception_handler(RequestValidationError,valitations_exception_handler)
app.add_exception_handler(Exception,exception_handler)

app.include_router(auth.router)
app.include_router(animals.router)
