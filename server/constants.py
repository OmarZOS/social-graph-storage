
import os

QUEUES = ['Twitter','Facebook','Youtube']

GRAPH_STORAGE_HOST = str(os.getenv("NEBULA_HOST"))
GRAPH_STORAGE_PORT = int(os.getenv("NEBULA_PORT"))
GRAPH_STORAGE_USER = str(os.getenv("NEBULA_USER"))
GRAPH_STORAGE_PASS = str(os.getenv("NEBULA_PASS"))

NEO4J_STORAGE_HOST = str(os.getenv("NEO4J_HOST"))
NEO4J_STORAGE_PORT = int(os.getenv("NEO4J_PORT"))
NEO4J_STORAGE_USER = str(os.getenv("NEO4J_USER"))
NEO4J_STORAGE_PASS = str(os.getenv("NEO4J_PASS"))
NEO4J_STORAGE_SCHEME = str(os.getenv("NEO4J_SCHEME"))

ELASTIC_HOST = str(os.getenv("ELASTICSEARCH_HOST"))
ELASTIC_PORT = str(os.getenv("ELASTICSEARCH_PORT"))
ELASTIC_SCHEME = str (os.getenv("ELASTIC_SCHEME"))

RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
RMQ_HOST = str(os.getenv("RABBIT_MQ_HOST"))
RMQ_PORT = int(os.getenv("RABBIT_MQ_PORT"))    
RMQ_EXCHG = str(os.getenv("RABBIT_MQ_EXCHG"))

