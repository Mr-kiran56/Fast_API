from pydantic import BaseModel
# from sqlalchemy import Column,INTEGER,Str
class Blog(BaseModel):
    id:int
    name:str
    age:int
 