from multiprocessing import Process
from fastapi import FastAPI
from listenerImplementation import rabbitMQ_Implementation as Listener
import data_handler as d_handler
import query_handler as q_handler
from models import *
from constants import *

# ----------- App initialisation -------------------------------------

app = FastAPI()

# on the other side, rabbitmq is mainly here to handle the system's internal data
listener = Process(target=Listener, args=(RMQ_EXCHG,))
# # then I'll tell you all about it when I see you again..
listener.start()


# ------------- Routes -----------------------------------------------

@app.get("/")
async def root():
    return {"message": "Welcome to phoros' services"}

@app.get("/storage")
def storage():
    return {"message": "Hello World"}

@app.post("/storage/query/data")
async def storage_submit_query(query: Query):
    return await q_handler.handle_query(query.api,query.content,query.roadmap)

@app.post("/storage/query/search")
async def storage_submit_query(query: Query):
    return await q_handler.handle_search(query.api,query.content)

@app.post("/storage/insert/graph")
async def storage_insert_graph(query: Query):
    return await d_handler.handle_data(query.api,query.content,query.roadmap)

