from constants import *

from elasticsearch import Elasticsearch



class elastic_wrapper:
    
    # es = Elasticsearch(f"http://{ELASTIC_HOST}:{ELASTIC_PORT}")
    def __init__(self): # name...,node/edge

        self.es = Elasticsearch([{'host': ELASTIC_HOST, 'port': ELASTIC_PORT}])
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
            self.es.index(index=f"{social_network_name}_node_{tag}",doc_type=f"{prop}",id=node[0],body=val)
    
    def insert_edge(self,social_network_name,tag,edge):
        
        for (prop,val) in edge[2].items():
            self.es.index(index=f"{social_network_name}_edge_{tag}",doc_type=f"{prop}",id=f"{edge[0]},{edge[1]}",body=val)
        
        



