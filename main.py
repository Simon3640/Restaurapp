#Python

#FastAPI
from fastapi import FastAPI

#Project
from Routes.routes import product

app = FastAPI()

app.include_router(product)

