from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from Config.db import engine, meta_data



Base = declarative_base()

meta_data.reflect()

class modelAdition(Base):
    __table__ = Table('Adiciones', meta_data,
                    autoload=True, autoload_with=engine)



