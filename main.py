#Python
from doctest import Example
from uuid import UUID
from typing import Optional, List
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field

#FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()

#Models

class Product(BaseModel):
    Product_id: UUID = Field(...)

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
    value: int = Field(
        ...,
        gt = 0,
        le = 100000000000,
        example = 20000
    )

class Ingredients(BaseModel):
    Ingridients_id : UUID = Field(...)

    name: str = Field(
        ...,
        min_length = 1,
        max_length = 45,
        example = "Cebolla"
    )

class Category(BaseModel):

    Category_id: UUID = Field(...)

    name: str = Field(
        ...,
        min_length = 1,
        max_length = 45,
        example = "Hamburguesas"
    )

class Add(BaseModel):
    Add_id: UUID = Field(...)
    
    name: str = Field(
        ...,
        min_length = 1,
        max_length = 45,
        example = "Tocineta"
    )
    value: int = Field(
        ...,
        gt = 0,
        le = 100000000000,
        example = 2000
    )

@app.get('/')
def Restaur_home():
    return {"Hola":'RestaurApp'}

@app.post('/product/new')
def create_product(
    product: Product = Body(...)
):
    return product