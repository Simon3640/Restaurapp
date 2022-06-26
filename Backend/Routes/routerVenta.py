from fastapi import APIRouter, Body, File, Form, Path, Query, Response, status, UploadFile, HTTPException
from pydantic import Field
from sqlalchemy import table
from Schemas.schemas import Venta

from UsefulFunctions import InsertINTO, showAllData, uploadData

from Models.ModelVenta import modelVenta

table = modelVenta.__table__

#Project

Route = APIRouter()

#Shortcuts

@Route.get(
    '/',
    status_code = status.HTTP_200_OK,
    summary = 'Permite la visualizacion de todas las ventas',
    tags = ['Ventas']
    )
async def todasLasVentas():
    
   return await showAllData(table) 

@Route.post('/',
    status_code = status.HTTP_201_CREATED,
    summary = 'Permite la creacion de una nueva venta',
    tags = ['Ventas']
    )
async def crearVenta(
    dataVenta: Venta = Body(...),
    ):
    dictVenta=dataVenta.dict()
    await uploadData(dictVenta,table)
    return {'Mensaje':'Venta creada'}