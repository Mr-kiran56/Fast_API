from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQL_DATABASE_NAME='sqlite:///./blog.db'
engine=create_engine(SQL_DATABASE_NAME,connect_args={"check_same_thread":False})
SessionMaker=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()

