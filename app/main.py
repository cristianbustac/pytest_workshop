from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api.api import router
#from debugger import initialize_fastapi_server_debugger_if_needed
from fastapi.middleware.cors import CORSMiddleware
from app.config import Settings

settings = Settings()

def create_application():
    #initialize_fastapi_server_debugger_if_needed()
    
    app = FastAPI(
        # title=settings.APP_TITLE,
        # description=settings.APP_DESCRIPTION,
        # version=settings.APP_VERSION,
    )
    app.include_router(router, prefix="/api")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_application()

register_tortoise(
    app,
    db_url= settings.POSTGRES_DATABASE_URL,
    modules={'models':['app.infra.postgres.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
