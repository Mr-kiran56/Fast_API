from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from files import models,schema
from database import get_db
from Hashing import pas_bct,Hash
from repositories import users
from routes import token
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(
    tags=['Login'],
    prefix='/login'
)

@router.post("/")
def Login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()  
    # OAuth2PasswordRequestForm gives 'username'
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!!")

    if not Hash.hash_verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


   
