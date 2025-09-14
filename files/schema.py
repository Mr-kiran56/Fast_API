from pydantic import BaseModel
from typing import List


class BlogSchema(BaseModel):
    title: str
    description: str

    class Config:
        from_attributes = True


class UserData(BaseModel): 
    name: str
    email: str
    password: str  


class User_Detail(BaseModel):  
    name: str
    email: str

    class Config:
        from_attributes = True


class GetData(User_Detail):  
    blogs: List[BlogSchema] = []

    class Config:
        from_attributes = True


class ShowBlog(BlogSchema):   
    creator: User_Detail

    class Config:
        from_attributes = True
