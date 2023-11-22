from fastapi import FastAPI

app=FastAPI()

@app.get("/home")
def home():
    return {"success":True,"message":"Hello world"}

@app.get("/about")
def about():
    return{"Name":"Nikita","Location":"Mumbai"}