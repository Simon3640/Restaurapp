#Python

#FastAPI
from fastapi import FastAPI

#Project
from Routes.routes import Route

app = FastAPI()

app.include_router(Route)

