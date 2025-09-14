from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from files import schema,models
from database import get_db


router=APIRouter()


@router.post("/newpost", status_code=status.HTTP_201_CREATED,tags=['blogs'])
def blog(request: schema.BlogSchema, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, description=request.description,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/getdata", status_code=status.HTTP_200_OK,response_model=List[schema.ShowBlog],tags=['blogs'])
def get_data(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get("/getbyid/{id}", status_code=status.HTTP_200_OK,response_model=schema.ShowBlog,tags=['blogs'])
def byid(id: int, db: Session=Depends(get_db)):
    data = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"This {id} is not found"
        )
    return data


@router.delete("/blogdelete/{id}", status_code=status.HTTP_200_OK,tags=['blogs'])
def deleted(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"This {id} is not found in db"
        )
    db.delete(blog)
    db.commit()
    return {"message": f"Id {id} is deleted!"}

@router.put("/blogupdate/{id}", status_code=status.HTTP_200_OK,tags=['blogs'])
def updatedata(id: int, request: schema.BlogSchema, db: Session = Depends(get_db)):
    blog_data = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"This {id} is not found in db"
        )
    
    blog_data.name = request.name
    blog_data.age = request.age
    
    db.commit()
    db.refresh(blog_data)
    return {"message": f"Id {id} updated successfully!", "data": blog_data}

    
