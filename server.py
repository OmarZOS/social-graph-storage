from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/storage_submit")
async def storage_submit():
    return {"message": "Hello World"}