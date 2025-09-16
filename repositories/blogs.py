from database import get_db
from Hashing import Hash
from fastapi import HTTPException,status
from files import models,schema
from sqlalchemy.orm import Session

class Blog:
    def Create_Blog(request:schema.BlogSchema,db:Session):
        new_blog = models.Blog(title=request.title, description=request.description,user_id=1)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog
    
    def Get_Blog(db:Session):
        blogs = db.query(models.Blog).all()
        return blogs
    
    def Get_Blog_By_Id(id,db:Session):
        data = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"This {id} is not foundd"
            )
        return data
    
    def Delete_Blog(id,db:Session):
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"This {id} is not found in db"
            )
        db.delete(blog)
        db.commit()
        return {"message": f"Id {id} is deleted!"}
    
    def Update_Blog(id,request:schema.BlogSchema,db:Session):
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

