#Python

#FastAPI
from fastapi import FastAPI

#Project
from Routes import routesProducts, routesCategory


app = FastAPI()

app.include_router(routesProducts.Route)
app.include_router(routesCategory.Route)

