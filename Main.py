from fastapi import FastAPI


app=FastAPI()
@app.get('/')
def Index():
    return {"dataa":{"kiran":"Btech","Age":20}}
@app.get("/blog/tranform")
def blog():
    return "thiis is blog"
@app.get("/blog/{id}")
def blog(id:int ):
    return {"data":{id}}

@app.get("/blog/{id}/number")
def blog():
    return {"data":{1,2,3,4,5}}


