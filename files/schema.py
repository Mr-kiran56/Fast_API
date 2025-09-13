from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    description: str

class User_Data(BaseModel):
    name:str
    email: str
    password: str

class Get_Data(BaseModel):
    name:str
    email:str
    users:List[Blog]=[]
    class Config:
        from_attributes:True


class ShowBlog(Blog):
    blog:Get_Data
    class Config:
        from_attributes = True
