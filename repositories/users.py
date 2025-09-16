from database import get_db
from Hashing import Hash
from fastapi import HTTPException,status
from files import models,schema
from sqlalchemy.orm import Session
class User:
    def User_setup(request:schema.UserData,db:Session):
        hashed_pass=Hash.hash_pass(request.password)
        user_data=models.User(name=request.name,email=request.email,password=hashed_pass)
        db.add(user_data)
        db.commit()
        db.refresh(user_data)
        return user_data
    
    def Get_User(id,db:Session):
        user_data=db.query(models.User).filter(models.User.id==id).first()
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this {id} user not Found !")
        return user_data