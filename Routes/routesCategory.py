#fastAPI
from typing import List, Optional
from fastapi import APIRouter, Body, File, Form, Query, Response, UploadFile, status
from pydantic import Field

#Project
from Schemas.schemas import Category, Product
from Config.db import engine
from Models.ModelCategory import modelCategory
from UsefulFunctions import GetColumn, Innerjoin, copiarImagen, deleteData, showAllData, uploadData

Route = APIRouter()
tableCategory = modelCategory.__table__

@Route.post(
    path = '/category/new',
    status_code = status.HTTP_201_CREATED,
    summary = 'Permite la creacion de un producto',
    tags = ['Categories']
    )
async def createCategory(
    category: Category = Body(...)
    ):
    """
    Path operation para crear una nueva categoria

    Este path operation recibe el esquema Category que tiene el siguiente contenido en formato JSON:

        Name: Nombre de la categoria

    Este path operation sube la informacion a la base de datos de MySQL:

        status code 201
        
    """

   
    data = category.dict()
    await uploadData(data, tableCategory)
    # category_id = await GetColumn('Categorias','id')[-1]
    # if image:
    #     file_name1 = f'images/GaleryCategories/Category_{category_id}.jpg'
    #     await copiarImagen(file_name1,image)
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
async def deleteCategory(
    category_id: int
):
    """Elimina una categoria de la base de datos

    Args:

        category_id (int, optional): Recibe el id de un producto

    Returns:

        remueve la categoria y devuelve HTTP 204
    """
    await deleteData(tableCategory, category_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@Route.get(
    path = '/categories',
    status_code = status.HTTP_200_OK,
    tags = ['client_views'],
    response_model = List[Category]
)
async def showCategories():
    result = await showAllData(tableCategory)
    return result
    

@Route.get(
    path = '/products/',
    status_code = status.HTTP_200_OK,
    tags = ['client_views'],
    response_model=List[Product]
)
def showProductsByCategory(
    category: int = Query(..., gt = 0, example = 0),
    ):
    result = Innerjoin(category)
    return result