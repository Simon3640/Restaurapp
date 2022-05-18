from uuid import uuid4
from shutil import copyfileobj

#fastAPI
from typing import List, Optional
from fastapi import APIRouter, Body, File, Form, Path, Query, Response, status
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
    tags = ['Categorys']
    )
def createCategory(
    dataCategory: Category = Body(...),
    ):
    """
    Path operation para crear una nueva categoria

    Este path operation recibe el esquema Category que tiene el siguiente contenido en formato JSON:

        Name: Nombre de la categoria

    Este path operation sube la informacion a la base de datos de MySQL:

        status code 201
        
    """

    with engine.connect() as conn:
        new_category = dataCategory.dict()
        conn.execute(tableCategory.insert().values(new_category))
        return Response(status_code=status.HTTP_201_CREATED)



@Route.delete(
    path = '/category/delete/{product_id}',
    status_code = status.HTTP_204_NO_CONTENT,
    summary = 'Elimina un producto',
    tags = ['Categorys']
)
def deleteProduct(
    Category : str = Query('No Category', enum=GetColumn('Categorias', 'Name'))
):
    """Elimina una categoria de la base de datos

    Args:

        category_id (int, optional): Recibe el id de un producto

    Returns:

        remueve el producto y devuelve HTTP 204
    """
    indexid = GetColumn('Categorias','Name').index(Category)
    category_id = GetColumn('Categorias','id')[indexid]
    with engine.connect() as conn:
        conn.execute(tableCategory.delete()\
        .where(tableCategory.c.id == category_id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)





