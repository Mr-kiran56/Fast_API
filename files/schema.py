from pydantic import BaseModel

class Blog(BaseModel):
    name: str
    age: int

class ShowBlog(Blog):
    class Config:
        from_attributes = True

class User_Data(BaseModel):
    email: str
    password: str
