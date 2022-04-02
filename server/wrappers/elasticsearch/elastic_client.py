from constants import *

from elasticsearch import Elasticsearch
from locator import singleton
from wrappers.StorageService import StorageService



@singleton
class elastic_wrapper(StorageService):
    
    def __init__(self,apiname="nichts"): # name...,node/edge

        self.es = Elasticsearch(f"{ELASTIC_SCHEME}://{ELASTIC_HOST}:{ELASTIC_PORT}")
        # self.index_name = index_name

    def _insert(self,index,type,id,body):
        self.es.index(index=index,
            type=type,
            id=id,
            body=body)
    
    def _get(self,index_name,id):
        self.es.get(index=index_name,id=id)
    
    def insert_node(self,social_network_name,tag,node):
        
        # for (prop,val) in node[1].items():
        #     print(val)
        self.es.index(index=(f"{social_network_name}_node_{tag}").lower(),id=node[0],body=node[1])
    
    def insert_edge(self,social_network_name,tag,edge):
        
        # for (prop,val) in edge[2].items():
            
        self.es.index(index=(f"{social_network_name}_edge_{tag}").lower(),id=f"{edge[0]},{edge[1]}",body=edge[2])

    def search(self,api,query):
        return self.es.search(query=query)["hits"]["hits"]
    
    def get(args):
        pass

    def test_connection(self):
        return self.es.ping()

    # just avoid this
    def queryData(self):
        pass
    
    # avoid this too..
    def saveData(self):
        pass    


