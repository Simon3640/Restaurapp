from Config.db import engine
from shutil import copyfileobj
from sqlalchemy import text

def GetColumn(Table : str,columname : str):
     with engine.connect() as conn:
         result = conn.execute(text(f'select {columname} from Retaurapp.{Table}'))
         result = [_[f"{columname}"] for _ in result]
     return result

def GetTable(Table:str):
    with engine.connect() as conn:
        result = conn.execute(text(f'SELECT * FROM Retaurapp.{Table}'))
        result_dict = result.mappings().all()
    return result_dict

async def InsertINTO(Table,data : tuple):
    with engine.connect() as conn:
        conn.execute(text('SET FOREIGN_KEY_CHECKS=0;'))
        conn.execute(text(f'INSERT INTO Retaurapp.{Table} VALUES (Null,'+str(data)[1:]))


async def showItemFromTable(Table,id : int):
    with engine.connect() as conn:
        result = conn.execute(Table.select()\
            .where(Table.c.id == id)).first()
    return result

async def copiarImagen(file_name : str,image):
    from os import path, makedirs
    makedirs(path.dirname(file_name),exist_ok=True)
    with open(file_name, "wb") as buffer:
            copyfileobj(image.file, buffer)
    

async def updateData(dictionary : dict, table, id : int):
    with engine.connect() as conn:
            conn.execute(
                table.update().values(dictionary)\
                    .where(table.c.id == id)
            )

async def uploadData(dictionary : dict, table):
    with engine.connect() as conn:
            conn.execute(
                table.insert().values(dictionary)
            )

async def deleteData(table, id : int):
    with engine.connect() as conn:
        conn.execute(table.delete()\
            .where(table.c.id == id))

async def showAllData(table):
    with engine.connect() as conn:
        result = conn.execute(table.select()).fetchall()
    return result


def Innerjoin(category_id : int):
    with engine.connect() as conn:
        result = conn.execute(text(f'SELECT Retaurapp.Producto.* \
        FROM Retaurapp.Producto \
            INNER JOIN Retaurapp.Categoria_producto ON Retaurapp.Producto.id = Retaurapp.Categoria_producto.id_producto \
            INNER JOIN Retaurapp.Categorias ON Retaurapp.Categoria_producto.id_categoria = Retaurapp.Categorias.id \
        where Retaurapp.Categorias.id = {category_id}'))
        result_dict = result.mappings().all()
    return result_dict
