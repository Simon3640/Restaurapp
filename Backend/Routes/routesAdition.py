from typing import Optional
from fastapi import APIRouter, status , Body, Response
from pydantic import Field

#Project
from Models.ModelAdition import modelAdition
from Schemas.schemas import Add
from UsefulFunctions import GetColumn, GetTable, copiarImagen, uploadData

Route = APIRouter()
tableAdition = modelAdition.__table__

@Route.post(
    path = '/',
    status_code = status.HTTP_201_CREATED,
    summary = 'Permite la creacion de un producto',
    tags = ['Adiciones'],
    )
async def createAdition(
    add : Add = Body(...),
    ):
    """
    Path operation para crear una nueva Adicion

    Este path operation recibe el esquema Add que tiene el siguiente contenido en formato JSON:

        Name: Nombre de la adicion
        Value: Valor de la adicion

    Este path operation sube la informacion a la base de datos de MySQL:

        status code 201
        
    """
    
    await uploadData(add.dict(), tableAdition)
    return Response(status_code=status.HTTP_201_CREATED)