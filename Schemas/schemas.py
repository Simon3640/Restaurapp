from typing import Optional, List
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[int]

    Product_name: str = Field(
        ...,
        min_length = 1,
        max_length = 150,
        example = "Hamburguesa"
    )

    Description: Optional[str] = Field(
        ...,
        min_length = 1,
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
        ...,
        example = "image/defaultimage.jpg"
    )

    Image_Galery: Optional[str] = Field(
        ...,
        example = "image/defaultimage.jpg"
    )

class ProductCategory(Product):
    Category: Optional[str] = Field(
        ...,
        )

class Ingredients(BaseModel):
    id : Optional[int]

    Name: str = Field(
        ...,
        min_length = 1,
        max_length = 45,
        example = "Cebolla"
    )

class Category(BaseModel):

    id: Optional[int]

    Name: str = Field(
        ...,
        min_length = 1,
        max_length = 45,
        example = "Hamburguesas"
    )
    img:str = Field(
        ...,
        min_length=1)

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
