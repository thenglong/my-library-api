from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import Base
from app.config.database import engine
from app.routes import book_route

# load .env file in development environment
load_dotenv()


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init database
Base.metadata.create_all(bind=engine)

app.include_router(book_route.router)


