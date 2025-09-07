from fastapi import FastAPI


app=FastAPI()
@app.get('/')
def Index():
    return {"dataa":{"kiran":"Btech","Age":20}}
