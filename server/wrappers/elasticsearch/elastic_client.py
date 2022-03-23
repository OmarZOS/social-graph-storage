from constants import *

from elasticsearch import Elasticsearch



class elastic_wrapper:
    
    def __init__(self): # name...,node/edge

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
        
        for (prop,val) in node[1].items():
            print(val)
            self.es.index(index=(f"{social_network_name}_node_{tag}_{prop}").lower(),id=node[0],body=val)
    
    def insert_edge(self,social_network_name,tag,edge):
        
        for (prop,val) in edge[2].items():
            self.es.index(index=(f"{social_network_name}_edge_{tag}_{prop}").lower(),id=f"{edge[0]},{edge[1]}",body=val)
        
    def search(api,content):
        pass
    
    def get(args):
        pass



