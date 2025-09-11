from sqlalchemy import Integer,Column,String
from database import Base

class Blog(Base):

    __tablename__="blog.db"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    age=Column(Integer)


