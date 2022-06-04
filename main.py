#Python

#FastAPI
from fastapi import FastAPI

#Project
from Routes import routesProducts, routesCategory, routesAdition
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], expose_headers=["*"])

app.include_router(routesProducts.Route)
app.include_router(routesCategory.Route)
app.include_router(routesAdition.Route)

