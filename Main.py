from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from typing import List
from files import models
from files import schema
from database import engine, SessionMaker
from passlib.context import CryptContext
app = FastAPI()

def get_db():
    db = SessionMaker()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

@app.post("/newpost", status_code=status.HTTP_201_CREATED,tags=['blogs'])
def blog(request: schema.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, description=request.descriptiotn,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/getdata", status_code=status.HTTP_200_OK,response_model=List[schema.ShowBlog],tags=['blogs'])
def get_data(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/getbyid/{id}", status_code=status.HTTP_200_OK,response_model=schema.ShowBlog,tags=['blogs'])
def byid(id: int, db: Session = Depends(get_db)):
    data = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"This {id} is not found"
        )
    return data


@app.delete("/blogdelete/{id}", status_code=status.HTTP_200_OK,tags=['blogs'])
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

@app.put("/blogupdate/{id}", status_code=status.HTTP_200_OK,tags=['blogs'])
def updatedata(id: int, request: schema.Blog, db: Session = Depends(get_db)):
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

    


pas_bct=CryptContext(schemes=['bcrypt'],deprecated="auto")

@app.post("/user",tags=['users'])
def User_data(request: schema.User_Data,db:Session=Depends(get_db)):
    hashed_pass=pas_bct.hash(request.password)
    user_data=models.User(name=request.name,email=request.email,password=hashed_pass)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


@app.get("/user_data{id}",response_model=schema.Get_Data,tags=['users'])
def get_user(id,db:Session=Depends(get_db)):
    
    user_data=db.query(models.User).filter(models.User.id==id).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this {id} user not Found !")
    return user_data




# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
