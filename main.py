from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from src.api.middleware.global_api_route_handler import GlobalApiRouteHandler
from src.api.middleware.global_exception_handler import app_exception_handler, exception_handler, valitations_exception_handler
from src.core.exceptions.app_exception_base import AppExceptionBase
from src.shared.config import enviroment
from src.api.endpoints import animals, auth
from scalar_fastapi import Layout, Theme, get_scalar_api_reference

config=enviroment.get_environment_settings()
app = FastAPI(
    docs_url='/docs',
    title=f"{config.APP_NAME}[{config.API_VERSION}]",
    description =f"{config.API_DESCRIPTION}",
    root_path=f"/{config.PATH_BASE}",
    version=f"{config.API_VERSION}"
    )

@app.get("/", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
    openapi_url=app.openapi_url,
    title=app.title,
    layout=Layout.CLASSIC,    
    dark_mode=True,
    persist_auth=True,
    theme=Theme.PURPLE
    )

app.router.route_class = GlobalApiRouteHandler
app.add_exception_handler(AppExceptionBase,app_exception_handler)
app.add_exception_handler(RequestValidationError,valitations_exception_handler)
app.add_exception_handler(Exception,exception_handler)

app.include_router(auth.router)
app.include_router(animals.router)