from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Deadmatch3640@localhost:3306/Retaurapp")

conn = engine.connect()

meta_data = MetaData(engine)