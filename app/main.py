from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.app_config import get_app_settings
from app.core.database import Base
from app.core.database import engine
from app.core.firebase_admin_config import init_firebase
from app.middlewares.custom_server_response_header import CustomServerResponseHeader
from app.routes import book_route, file_route, admin_user_route


def get_application() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_middleware(CustomServerResponseHeader, server_name="just-a-python-assigment")

    application.include_router(book_route.router)
    application.include_router(admin_user_route.router)
    application.include_router(file_route.router)

    return application


app = get_application()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    init_firebase()


@app.on_event("shutdown")
def shutdown_event():
    print("Application has been shut down")
