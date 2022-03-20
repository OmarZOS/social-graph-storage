import subprocess

from fastapi import FastAPI
from listenerImplementation import rabbitMQ_Implementation
from constants import *

app = FastAPI();

listener = subprocess.run(["python3","listenerImplementation.py"])
# listener = rabbitMQ_Implementation()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/storage_submit")
async def storage_submit():
    return {"message": "Hello World"}
