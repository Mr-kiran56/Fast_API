from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from files import models
from files import schema
from database import engine, SessionMaker
from passlib.context import CryptContext
from routes import blogs
from database import get_db
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(blogs.router)

pas_bct=CryptContext(schemes=['bcrypt'],deprecated="auto")

@app.post("/user",tags=['users'])
def User_data(request: schema.UserData,db:Session=Depends(get_db)):
    hashed_pass=pas_bct.hash(request.password)
    user_data=models.User(name=request.name,email=request.email,password=hashed_pass)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


@app.get("/user_data{id}",response_model=schema.GetData,tags=['users'])
def get_user(id,db:Session=Depends(get_db)):
    
    user_data=db.query(models.User).filter(models.User.id==id).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this {id} user not Found !")
    return user_data




# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
