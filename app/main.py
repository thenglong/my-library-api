import json
import os

import firebase_admin
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import credentials

from app.core.config import get_app_settings
from app.core.database import Base
from app.core.database import engine
from app.middlewares.custom_server_response_header import CustomServerResponseHeader
from app.routes import book_route, file_route

# Load env
load_dotenv()

# Init firebase admin
service_account_json = os.environ.get("FIREBASE_SERVICE_ACCOUNT_JSON")
bucket_url = os.environ.get('FIREBASE_STORAGE_BUCKET_URL')
service_account = json.loads(service_account_json)
cred = credentials.Certificate(cert=service_account)
default_app = firebase_admin.initialize_app(cred, {
    'storageBucket': bucket_url,
})

try:
    print(f"Firebase Admin initialize with project id -> {default_app.project_id}")
except:
    print("Cannot init firebase")


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

    application.add_middleware(CustomServerResponseHeader, server_name="")

    application.include_router(book_route.router)
    application.include_router(file_route.router)

    return application


Base.metadata.create_all(bind=engine)
app = get_application()
