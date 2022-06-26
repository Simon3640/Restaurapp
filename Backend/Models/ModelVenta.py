from sqlalchemy import JSON, DateTime, Integer, String, Column
from sqlalchemy.sql import func
from Config.db import Base


class modelVenta(Base):
    __tablename__ = 'Ventas'
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, nullable=True)
    Informacion = Column(JSON, nullable=False)
    Fecha = Column(DateTime, default=func.now())
    Estado = Column(String(255), nullable=False)
    def __init__(self, id_cliente, Informacion):
        self.id_cliente = id_cliente
        self.Informacion = Informacion
        self.Estado = 'Pendiente'

