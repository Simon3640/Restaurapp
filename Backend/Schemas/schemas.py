from datetime import datetime
from doctest import Example
from typing import Optional, List
from pydantic import BaseModel, Field, Json


#TODO: Producto

class Product(BaseModel):
    id: Optional[int]

    Name: str = Field(
        ...,
        min_length = 1,
        max_length = 150,
        example = "Hamburguesa"
    )

    Description: Optional[str] = Field(
        ...,
        min_length = 20,
        max_length = 300,
        example = "Deliciosa hamburguesa hecha con carne de res, queso americano y lechuga romana"
    )
    Short_Description: Optional[str] = Field(
        ...,
        min_length = 1,
        max_length = 100,
        example = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean m"
    )
    Value: int = Field(
        ...,
        gt = 0,
        le = 100000000000,
        example = 20000
    )

    Image: Optional[str] = Field(
        example = "image/defaultimage.jpg"
    )

    Image_Galery: Optional[List[str]] = Field(
        example = "image/defaultimage.jpg"
    )


    Ingredients : Optional[List[str]] = Field(
        example = ['Tocineta', 'Carne de res', 'Queso americano', 'Lechuga romana']
    )


class ProductCategory(Product):
    Category: Optional[int] = Field(
        ...,
    )

class ProductForCategory(Product):
    Image_Galery: Optional[Json] = Field( example = 'image/defaultimage.jpg')
    Ingredients : Optional[Json] = Field( example = 'Tocineta')


#TODO: Categoria


class Category(BaseModel):

    id: Optional[int]

    Name: str = Field(
        ...,
        min_length = 1,
        max_length = 255,
        example = "Hamburguesas"
    )
    Image:str = Field(
        min_length=1)


#TODO: Adiciones

class Add(BaseModel):
    id: Optional[int]
    
    Name: str = Field(
        ...,
        min_length = 1,
        max_length = 45,
        example = "Tocineta"
    )
    Value: int = Field(
        ...,
        gt = 0,
        le = 100000000000,
        example = 2000
    )


#TODO: Venta

class Venta(BaseModel):
    id: Optional[int]

    id_cliente: Optional[int] = Field(
        ...,
        gt = 0,
        le = 100000000000,
        example = 1
    )

    Informacion: List[Json] = Field(
        ...,
        example = '''[{
            "Product_id": 1,
            "Quantity": 1,
            "Additions": [
                1,2,3,4
                ],
            "Ingredients": [
                'Tocineta','Carne de res','Queso americano','Lechuga romana'
                ]
            },
            {
            "Product_id": 2,
            "Quantity": 2,
            "Additions": [
                1,2,3,4
                ],
            "Ingredients": [
                'Tocineta','Carne de res','Queso americano','Lechuga romana'
                ]
            }
        ]'''
    )

    Fecha: Optional[datetime] = Field(
        ...,
        example = "2020-01-01T00:00:00.000Z"
    )

    Estado: Optional[str] = Field(
        ...,
        example = "Pendiente"
    )