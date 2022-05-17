#python
from uuid import uuid4
from shutil import copyfileobj

#fastAPI
from typing import List, Optional
from fastapi import APIRouter, Body, File, Form, Path, Response, status, UploadFile, HTTPException
from pydantic import Field


#Project
from Schemas.schemas import Product
from Config.db import engine
from Models.models import modelProduct

Route=APIRouter()

#Shortcuts
tableProduct= modelProduct.__table__



@Route.get('/user')
def Home():
    return {'Hola':'Mundo'}



#Todo lo relacionado a la edicion de la base de datos de los productos
##Creamos un producto
@Route.post(
    path = '/product/new',
    status_code = status.HTTP_201_CREATED,
    summary = 'Permite la creacion de un producto',
    tags = ['Products']
    )
def createProduct(
    dataProduct: Product = Body(...),
    ):
    """
    Path operation para crear un nuevo producto

    Este path operation recibe el esquema Product que tiene el siguiente contenido en formato JSON:

        Product_name: Nombre del producto * - maximo 50 caracteres 
        Description: Descripcion del producto - maximo 300 caracteres
        Short_Description: Descripcion corta corta del producto * - maximo 100 caracteres
        Value: Precio del producto * 

    Este path operation sube la informacion basica del producto a la base de datos de MySQL:

        status code 201
        
    """
    
    with engine.connect() as conn:
        new_product = dataProduct.dict()
        conn.execute(tableProduct.insert().values(new_product))
        return Response(status_code=status.HTTP_201_CREATED)


##Elimina un producto

@Route.delete(
    path = '/product/delete/{product_id}',
    status_code = status.HTTP_204_NO_CONTENT,
    summary = 'Elimina un producto',
    tags = ['Products']
)
def deleteProduct(
    product_id: int
):
    """Elimina un producto de la base de datos

    Args:

        product_id (int, optional): Recibe el id de un producto

    Returns:

        remueve el producto y devuelve HTTP 204
    """
    with engine.connect() as conn:
        conn.execute(tableProduct.delete()\
        .where(tableProduct.c.Product_id == product_id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)



##Actualiza las imagenes del producto
@Route.put(
    path = '/product/update_images/{product_id}',
    status_code = status.HTTP_200_OK,
    summary = 'Sube las imágenes de un producto',
    tags = ['Products']
)
def updateImages(
    product_id: int = Path(
        ...,
        gt = 0,
        example = 0
    ),
    image: UploadFile = File(None),
    galery: List[UploadFile] = File(None)
    ):
    """
    Este path operation permite al usuario subir y actualizar las imagenes de su producto

    Args:
        
        product_id (int, optional): id del producto, tomaremos como default el ultimo con 
                                    el fin de integrarlo en la misma vista de la creacion del producto.
        image (UploadFile, optional): unica imagen, imagen principal.
        galery (List[UploadFile], galeria de imagenes, las necesarias para el cliente.

    Raises:
        
        HTTPException: cuando el archivo subido no es jpeg o png

    Returns:
        
        Sube la imagen al directori local de imagenes y las organiza en carpetas con el respectivo id del producto
        Renombra las imagenes y sube el string de la ubicacion a la base de datos
    """
    
    if image.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Only .jpeg or .png  files allowed")
    
    from os import makedirs, path
    
    codeim = uuid4()
    file_name1 = f'images/GaleryProduct{product_id}/{codeim}.jpg'
    makedirs(path.dirname(file_name1), exist_ok=True)
   
    with open(file_name1, "wb") as buffer:
        copyfileobj(image.file, buffer)
    
    Gcodeim = []

    for imG in galery:
        gcodeim = uuid4()
        Gcodeim += [f'{gcodeim}']
        file_name = f'images/GaleryProduct{product_id}/{gcodeim}.jpg'
        with open(file_name, "wb") as buffer:
            copyfileobj(imG.file, buffer)
    
    with engine.connect() as conn:
        conn.execute(tableProduct.update()\
            .values(Image = codeim, Image_Galery = str(Gcodeim))\
                .where(tableProduct.c.Product_id == product_id))
        return Response(status_code=status.HTTP_201_CREATED)


##Actualiza la informacion de un producto

@Route.put(
    path = '/product/update/{product_id}',
    status_code = status.HTTP_200_OK,
    summary = 'actualiza la informacion de un prodcuto',
    tags = ['Products']
)
def updateProduct(
    dataProduct: Product,
    product_id: int
):
    """Este path operation realiza una actualizacion en la base de datos del producto

    Args:

        dataProduct (Product): informacion actualizada del producto
        product_id (int): id del producto objetivo

    Returns:

        actualiza la base de datos y devuelve un response HTTP 200
    """
    upDataProduct=dataProduct.dict()
    with engine.connect() as conn:
        conn.execute(
            tableProduct.update().values(upDataProduct)\
                .where(tableProduct.c.Product_id == product_id)
        )
    return Response(status_code= status.HTTP_200_OK)


##Categorias
###Crear categoria



#Vistas de los productos
##Vista completa de los productos
@Route.get(
    path='/',
    response_model=List[Product],
    tags = ['client_views'],
    summary = 'Permite visualizar todos los productos en la base de datos'
)
def showProducts():
    """Crea la vista de los productos en la base de datos

    Returns:
        
        Lista de productos
    """
    with engine.connect() as conn:
        result = conn.execute(tableProduct.select()).fetchall()
    return result

##Vista de un unico producto
@Route.get(
    path = '/product/{product_id}',
    response_model = Product,
    tags = ['client_views'],
    summary = 'Permite visualizar un unico producto'
)
def showProduct(product_id: int):
    """AI is creating summary for showProduct

    Args:
        
        recibe el id del producto que se desea visualizar

    Returns:
        
        informacion del producto con el id seleccionado
    """
    with engine.connect() as conn:
        result = conn.execute(tableProduct.select()\
            .where(tableProduct.c.Product_id == product_id)).first()
    return result





