from sqlalchemy import Integer,Column,String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Blog(Base):

    __tablename__="blog.db"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    title=Column(String)
    description=Column(String)

blog=relationship("User",back_populates="users")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    email = Column(String)
    password = Column(String)

users=relationship("Blog",back_populates="blog")