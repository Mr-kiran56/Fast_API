from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from files import models,schema
from database import get_db
from Hashing import pas_bct,Hash
from repositories import users
router=APIRouter(
    tags=['Users'],
    prefix='/users'
)


@router.post("/")
def User_data(request: schema.UserData,db:Session=Depends(get_db)):
    return users.User.User_setup(request,db)
   

@router.get("/{id}",response_model=schema.GetData)
def get_user(id,db:Session=Depends(get_db)):
   return users.User.Get_User(id,db)
