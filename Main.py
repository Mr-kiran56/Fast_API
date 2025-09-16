from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from typing import List
from files import models
# from files import schema
from database import engine, SessionMaker
from routes import blogs,users,login
# from database import get_db
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(login.router)
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
