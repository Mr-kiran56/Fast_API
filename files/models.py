from sqlalchemy import Integer,Column,String
from database import Base

class Blog(Base):

    __tablename__="blog"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    age=Column(Integer)


class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    email=Column(String)
    password=Column(String)