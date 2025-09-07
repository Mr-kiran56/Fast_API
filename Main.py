from fastapi import FastAPI


app=FastAPI()
@app.get('/')
def Index():
    return {"data":{"kiran":"Btech","Age":20}}
