from sqlalchemy import Integer, String, Column
from Config.db import  meta_data, Base


meta_data.reflect()

class modelCategory(Base):
    # __table__ = Table('Categoria', meta_data,
    #                 autoload=True, autoload_with=engine)
    __tablename__ = 'Categoria'
    id = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Image = Column(String(1000), nullable=False)

    def __init__(self, Name, Image):
        self.Name= Name
        self.Image = Image