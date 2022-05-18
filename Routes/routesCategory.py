from uuid import uuid4
from shutil import copyfileobj

#fastAPI
from typing import List, Optional
from fastapi import APIRouter, Body, File, Form, Path, Query, Response, UploadFile, status
from pydantic import Field

#Project
from Schemas.schemas import Category
from Config.db import engine
from Models.ModelCategory import modelCategory
from UsefulFunctions import GetColumn, InsertINTO

Route = APIRouter()
tableCategory = modelCategory.__table__

@Route.post(
    path = '/category/new',
    status_code = status.HTTP_201_CREATED,
    summary = 'Permite la creacion de un producto',
    tags = ['Categories']
    )
def createCategory(
    category_name: str = Form(...),
    image: UploadFile = File(None)
    ):
    """
    Path operation para crear una nueva categoria

    Este path operation recibe el esquema Category que tiene el siguiente contenido en formato JSON:

        Name: Nombre de la categoria

    Este path operation sube la informacion a la base de datos de MySQL:

        status code 201
        
    """

    
    category_id = GetColumn('Producto','Product_id')[-1]+1

    file_name1 = f'images/GaleryCategories/Category_{category_id}.jpg'
    with open(file_name1, "wb") as buffer:
        copyfileobj(image.file, buffer)
   

    with engine.connect() as conn:
        conn.execute(tableCategory.insert().values(Name=category_name))
        return Response(status_code=status.HTTP_201_CREATED)



@Route.delete(
    path = '/category/delete/{category_id}',
    status_code = status.HTTP_204_NO_CONTENT,
    summary = 'Elimina un producto',
    tags = ['Categories']
)
def deleteCategory(
    category_id: int
):
    """Elimina una categoria de la base de datos

    Args:

        category_id (int, optional): Recibe el id de un producto

    Returns:

        remueve la categoria y devuelve HTTP 204
    """
    with engine.connect() as conn:
        conn.execute(tableCategory.delete()\
        .where(tableCategory.c.id == category_id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@Route.get(
    path = '/categories',
    status_code = status.HTTP_200_OK,
    tags = ['Categories']
)
def showCategories():
    with engine.connect() as conn:
        result = conn.execute(tableCategory.select()).fetchall()
    return result
    


