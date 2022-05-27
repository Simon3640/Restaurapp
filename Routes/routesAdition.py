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
    path = '/adition/new',
    status_code = status.HTTP_201_CREATED,
    summary = 'Permite la creacion de un producto',
    tags = ['Adds'],
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

# @Route.put(
#     path = '/category/update/{category_id}',
#     status_code = status.HTTP_200_OK,
#     summary = 'Permite la actualización de una categoría',
#     tags = ['Categories']
# )
# async def updateCategory(
#     category_id : int,
#     dataCategory : Optional[str] = Form(min_length=1, max_length=45, default=None),
#     image : Optional[UploadFile] = File(None)
# ):
#     if image:
#         file_name1 = f'images/GaleryCategories/Category_{category_id}.jpg'
#         await copiarImagen(file_name1,image)
    
#     if dataCategory:
#         with connect() as conn:
#             conn.execute(tableCategory.update().values(Name=dataCategory)\
#                 .where(tableCategory.c.id == category_id))
#     return Response(status_code = status.HTTP_200_OK)

# @Route.delete(
#     path = '/category/delete/{category_id}',
#     status_code = status.HTTP_204_NO_CONTENT,
#     summary = 'Elimina un producto',
#     tags = ['Categories']
# )
# def deleteCategory(
#     category_id: int
# ):
#     """Elimina una categoria de la base de datos

#     Args:

#         category_id (int, optional): Recibe el id de un producto

#     Returns:

#         remueve la categoria y devuelve HTTP 204
#     """
#     with engine.connect() as conn:
#         conn.execute(tableCategory.delete()\
#         .where(tableCategory.c.id == category_id))
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @Route.get(
#     path = '/categories',
#     status_code = status.HTTP_200_OK,
#     tags = ['client_views']
# )
# def showCategories():
#     with engine.connect() as conn:
#         result = conn.execute(tableCategory.select()).fetchall()
#     return result