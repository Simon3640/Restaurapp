from Config.db import engine

from sqlalchemy import text


def GetColumn(Table,columname):
     with engine.connect() as conn:
         result = conn.execute(text(f'select {columname} from Retaurapp.{Table}'))
         result = [_[f"{columname}"] for _ in result]
     return result

def InsertINTO(Table,data):
    with engine.connect() as conn:
        conn.execute(text(f'INSERT INTO Retaurapp.{Table} VALUES (Null,'+str(data)[1:]))