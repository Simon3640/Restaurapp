#Python

#FastAPI
from fastapi import FastAPI

#Project
from Routes import routesProducts, routesCategory, routesAdition


app = FastAPI()

app.include_router(routesProducts.Route)
app.include_router(routesCategory.Route)
app.include_router(routesAdition.Route)

