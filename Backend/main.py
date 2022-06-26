#Python

#FastAPI
from fastapi import FastAPI

#Project
from Routes import routerVenta, routesProducts, routesCategory, routesAdition
from starlette.middleware.cors import CORSMiddleware
from Config.db import Base, engine
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], expose_headers=["*"])

Base.metadata.create_all(bind=engine)

app.include_router(routesProducts.Route)
app.include_router(routesCategory.Route)
app.include_router(routesAdition.Route, prefix='/Adiciones')
app.include_router(routerVenta.Route, prefix='/ventas')

