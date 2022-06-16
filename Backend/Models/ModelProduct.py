from email.policy import default
from sqlalchemy import JSON, Integer, Column, String
from sqlalchemy.types import ARRAY
from Config.db import meta_data, Base


meta_data.reflect()

class modelProduct(Base):
    # __table__ = Table('Producto', meta_data,
    #                 autoload=True, autoload_with=engine)
    __tablename__ = 'Producto'
    id = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Description = Column(String(300), nullable=False)
    Short_Description = Column(String(100), nullable=False)
    Value = Column(Integer, nullable=False)
    Image = Column(String(1000), nullable=False)
    Image_Galery = Column(JSON, nullable=True, default=None)
    Ingredients = Column(JSON, nullable=True, default='Image/defaultimage.jpg')

    def __init__(self, Name, Description, Short_Description, Value,Ingredients, Image, Image_Galery):
        self.Name= Name
        self.Description = Description
        self.Short_Description = Short_Description
        self.Value = Value
        self.Image = Image
        self.Image_Galery = Image_Galery
        self.Ingredients = Ingredients


