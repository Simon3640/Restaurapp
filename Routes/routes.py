#python
from http.client import HTTPException
from posixpath import dirname
from uuid import uuid4
from shutil import copyfileobj

#fastAPI
from typing import List, Optional
from fastapi import APIRouter, Body, File, Path, Response, status, UploadFile, HTTPException


#Project
from Schemas.schemas import Product
from Config.db import engine
from Models.models import modelProduct

product=APIRouter()

@product.get('/')
def Home():
    return {'Hola':'Mundo'}

##Creamos un producto
@product.post(
    path = '/product/new',
    status_code = status.HTTP_201_CREATED,
    summary = 'Product Created',
    tags = ['Products']
    )
def createProduct(
    dataProduct: Product,
    ):

    
    with engine.connect() as conn:
        new_product = dataProduct.dict()
        conn.execute(modelProduct.__table__.insert().values(new_product))
        return Response(status_code=status.HTTP_201_CREATED)



##Actualiza las imagenes del producto
@product.put(
    path = '/product/update_images/{product_id}',
    status_code = status.HTTP_200_OK,
    summary = 'Sube las imágenes de un producto',
    tags = ['Products']
)
def Update_images(
    product_id: int = Path(
        ...,
        gt=0
    ),
    image: UploadFile = File(None),
    galery: List[UploadFile] = File(None)
    ):
    
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
        conn.execute(modelProduct.__table__.update()\
            .values(Image = codeim, Image_Galery = str(Gcodeim))\
                .where(modelProduct.__table__.c.Product_id == product_id))
        return Response(status_code=status.HTTP_201_CREATED)

