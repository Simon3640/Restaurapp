from sqlite3 import connect
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
from UsefulFunctions import GetColumn, InsertINTO, copiarImagen

Route = APIRouter()
tableCategory = modelCategory.__table__

@Route.post(
    path = '/category/new',
    status_code = status.HTTP_201_CREATED,
    summary = 'Permite la creacion de un producto',
    tags = ['Categories']
    )
async def createCategory(
    category_name: str = Form(..., max_length = 45, min_length = 1),
    image: Optional[UploadFile] = File(None)
    ):
    """
    Path operation para crear una nueva categoria

    Este path operation recibe el esquema Category que tiene el siguiente contenido en formato JSON:

        Name: Nombre de la categoria

    Este path operation sube la informacion a la base de datos de MySQL:

        status code 201
        
    """

    
    category_id = GetColumn('Producto','id')[-1]+1
    if image:
        file_name1 = f'images/GaleryCategories/Category_{category_id}.jpg'
        await copiarImagen(file_name1,image)
   

    with engine.connect() as conn:
        conn.execute(tableCategory.insert().values(Name=category_name))
        return Response(status_code=status.HTTP_201_CREATED)


@Route.put(
    path = '/category/update/{category_id}',
    status_code = status.HTTP_200_OK,
    summary = 'Permite la actualización de una categoría',
    tags = ['Categories']
)
async def updateCategory(
    category_id : int,
    dataCategory : Optional[str] = Form(min_length=1, max_length=45, default=None),
    image : Optional[UploadFile] = File(None)
):
    if image:
        file_name1 = f'images/GaleryCategories/Category_{category_id}.jpg'
        await copiarImagen(file_name1,image)
    
    if dataCategory:
        with connect() as conn:
            conn.execute(tableCategory.update().values(Name=dataCategory)\
                .where(tableCategory.c.id == category_id))
    return Response(status_code = status.HTTP_200_OK)

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
    


