#python
from email.policy import default
from uuid import uuid4

#fastAPI
from typing import List, Optional
from fastapi import APIRouter, Body, File, Form, Path, Query, Response, status, UploadFile, HTTPException
from pydantic import Field

#Project
from Schemas.schemas import Product, ProductCategory
from Config.db import engine
from Models.ModelProduct import modelProduct
from UsefulFunctions import GetColumn, InsertINTO, copiarImagen, deleteData, showAllData, showItemFromTable, updateData, uploadData

Route=APIRouter()

#Shortcuts
tableProduct = modelProduct.__table__


#Usable Functions

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
async def createProduct(
    dataProduct: ProductCategory = Body(...),
    ):
    """
    Path operation para crear un nuevo producto

    Este path operation recibe el esquema Product que tiene el siguiente contenido en formato JSON:

        Product_name: Nombre del producto * - maximo 50 caracteres 
        Description: Descripcion del producto - maximo 300 caracteres
        Short_Description: Descripcion corta corta del producto * - maximo 100 caracteres
        Value: Precio del producto * 

        Categoria

    Este path operation sube la informacion basica del producto a la base de datos de MySQL:

        status code 201
        
    """
    dictProduct=dataProduct.dict()
    Category = dictProduct['Category']
    del dictProduct['Category']
    
    indexid = GetColumn('Categorias','Name').index(Category)
    idCategoria = GetColumn('Categorias','id')[indexid]
    

    await uploadData(dictProduct,tableProduct)

    idProduct = GetColumn('Producto','id')[-1]

    await InsertINTO('Categoria_producto',(idCategoria,idProduct))

    return Response(status_code=status.HTTP_201_CREATED)


##Elimina un producto

@Route.delete(
    path = '/product/delete/{product_id}',
    status_code = status.HTTP_204_NO_CONTENT,
    summary = 'Elimina un producto',
    tags = ['Products']
)
async def deleteProduct(
    product_id: int
):
    """Elimina un producto de la base de datos

    Args:

        product_id (int, optional): Recibe el id de un producto

    Returns:

        remueve el producto y devuelve HTTP 204
    """
    
    await deleteData(tableProduct, product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)



##Actualiza las imagenes del producto
@Route.put(
    path = '/product/update_images/{product_id}',
    status_code = status.HTTP_200_OK,
    summary = 'Sube las imágenes de un producto',
    tags = ['Products']
)
async def updateImages(
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
    
    file_name1 = f'images/GaleryProduct{product_id}/Principal_Image.jpg'
   
    await copiarImagen(file_name1,image)

    for _,imG in enumerate(galery):
        file_name = f'images/GaleryProduct{product_id}/Image{_}.jpg'
        await copiarImagen(file_name,imG)
    
    return Response(status_code = status.HTTP_200_OK)

##Actualiza la informacion de un producto

@Route.put(
    path = '/product/update/{product_id}',
    status_code = status.HTTP_200_OK,
    summary = 'actualiza la informacion de un prodcuto',
    tags = ['Products']
)
async def updateProduct(
    product_id: int,
    dataProduct: Optional[Product] = Body(default=None),
    Category : Optional[str] = Query(default=None, enum=GetColumn('Categorias', 'Name')),
):
    """Este path operation realiza una actualizacion en la base de datos del producto

    Args:

        dataProduct (Product): informacion actualizada del producto
        product_id (int): id del producto objetivo

    Returns:

        actualiza la base de datos y devuelve un response HTTP 200
    """
    if Category:
        indexid = GetColumn('Categorias','Name').index(Category)
        idCategoria = GetColumn('Categorias','id')[indexid]
        InsertINTO('Categoria_producto',(idCategoria,product_id))
    if dataProduct:
        upDataProduct=dataProduct.dict()
        await updateData(upDataProduct,tableProduct,product_id)
    return Response(status_code= status.HTTP_200_OK)



#Vistas de los productos
##Vista completa de los productos
@Route.get(
    path='/products',
    response_model=List[Product],
    tags = ['client_views'],
    summary = 'Permite visualizar todos los productos en la base de datos',
    )
async def showProducts():
    """Crea la vista de los productos en la base de datos

    Returns:
        
        Lista de productos
    """
    result = await showAllData(tableProduct)
    return result

##Vista de un unico producto
@Route.get(
    path = '/product/{product_id}',
    response_model = Product,
    tags = ['client_views'],
    summary = 'Permite visualizar un unico producto'
)
async def showProduct(product_id: int):
    """AI is creating summary for showProduct

    Args:
        
        recibe el id del producto que se desea visualizar

    Returns:
        
        informacion del producto con el id seleccionado
    """
    result = await showItemFromTable(tableProduct,product_id)
    
    return result





