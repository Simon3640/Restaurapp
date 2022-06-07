from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:Deadmatch3640@localhost:3306/Restaurapp")

conn = engine.connect()

Base = declarative_base()

meta_data = MetaData(engine)