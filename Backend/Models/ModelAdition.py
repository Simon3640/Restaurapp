from sqlalchemy import Integer, String, Column
from Config.db import meta_data, Base



meta_data.reflect()

class modelAdition(Base):
    # __table__ = Table('Adiciones', meta_data,
    #                 autoload=True, autoload_with=engine)
    __tablename__ = 'Adiciones'
    id = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Value = Column(Integer, nullable=False)
    
    def __init__(self, Name, Value):
        self.Name= Name
        self.Value = Value



