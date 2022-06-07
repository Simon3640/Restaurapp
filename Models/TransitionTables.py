from sqlalchemy import Integer, Column
from Config.db import meta_data, Base

meta_data.reflect()

class modelCategoryProduct(Base):
    __tablename__ = 'Categoria_producto'
    id = Column(Integer, primary_key=True)
    id_categoria = Column(Integer, nullable=False)
    id_producto = Column(Integer, nullable=False)

    def __init__(self, id_categoria, id_producto):
        self.id_categoria = id_categoria
        self.id_producto = id_producto

    