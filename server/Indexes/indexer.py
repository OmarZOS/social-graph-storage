
import os
from elasticsearch import Elasticsearch

ELASTIC_HOST =  str(os.getenv("ELASTIC_HOST"))
ELASTIC_PORT =  int(os.getenv("ELASTIC_PORT"))

class Indexer(object):
    
    def __init__(self,index_name):# name...,node/edge
        
        self.es = Elasticsearch([{'host': ELASTIC_HOST, 'port': ELASTIC_PORT}])

        self.index_name = index_name

    def index(self,doc_type, doc_id=None, doc_body=None):
        self.es.index(
            index=self.index_name,
            doc_type=doc_type,
            id=doc_id,
            body=doc_body)


