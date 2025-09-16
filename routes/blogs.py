from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from files import schema,models
from database import get_db
from repositories import blogs
from routes import oauth2
router=APIRouter(
    tags=['Blogs'],
    prefix='/blogs'
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def blog(request: schema.BlogSchema, db: Session = Depends(get_db)):
   return blogs.Blog.Create_Blog(request,db)


@router.get("/", status_code=status.HTTP_200_OK,response_model=List[schema.ShowBlog])
def get_data(db: Session = Depends(get_db),get_current_user:schema.User_Detail=Depends(oauth2.get_current_user)):
   return blogs.Blog.Get_Blog(db)


@router.get("/{id}", status_code=status.HTTP_200_OK,response_model=schema.ShowBlog)
def byid(id: int, db: Session=Depends(get_db)):
    return blogs.Blog.Get_Blog_By_Id(id,db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def deleted(id: int, db: Session = Depends(get_db)):
    return blogs.Blog.Delete_Blog(id,db)
    

@router.put("/{id}", status_code=status.HTTP_200_OK)
def updatedata(id: int, request: schema.BlogSchema, db: Session = Depends(get_db)):
    return blogs.Blog.Update_Blog(id,request,db)
   
    
