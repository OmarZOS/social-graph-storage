from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config
from constants import *

class nebula_client(object):
    
    # define a config
    config = Config()
    config.max_connection_pool_size = 10
    
    # init connection pool
    connection_pool = ConnectionPool()
    
    # # if the given servers are ok, return true, else return false
    # ok = connection_pool.init([(GRAPH_STORAGE_HOST, GRAPH_STORAGE_PORT)], config)
    
    connection_pool.init([(GRAPH_STORAGE_HOST,GRAPH_STORAGE_PORT)], config)

    session = None
    
    _get_space_name = lambda self,x : f"{x}_graph"

    def __init__(self,space):
        # get session from the pool
        self.session = self.connection_pool.get_session(GRAPH_STORAGE_USER, GRAPH_STORAGE_PASS)
        
        # select space
        self.session.execute(f"CREATE SPACE IF NOT EXISTS {self._get_space_name(space)} ( vid_type = INT64 )")
        try:
            self.session.execute(f"USE {self._get_space_name(space)}")
        except :
            print(f"Can't connect to space: {space} ")
            

    def __del__(self):
        # close the pool
        self.connection_pool.close()
        print("Session ended, farewell nebula..")
    
    def insert_node(self,social_network_name,tag,node):
        
        labels=f"INSERT VERTEX IF NOT EXISTS {tag}("
        values=f"VALUES {node[0]}:("
        for (prop,val) in node[1].items():
            labels+=f"{prop},"
            if(int(val)):
                values+=f"{val},"
            else:
                values+=f"\"{val}\","
            query=labels[:-1]+") "+ values[:-1]+")"
        # check if the there were any inserted fields
        if(labels[-1]==','):
            query=labels[:-1]+") "+ values[:-1]+")"
        else:
            query=labels+") "+ values+")"
        result = self.session.execute(query)
        return result

    def insert_edge(self,social_network_name,edge_type,edge):
        labels=f"INSERT EDGE IF NOT EXISTS {edge_type}("
        values=f"VALUES {edge[0]} -> {edge[1]}:("
        for (prop,val) in edge[2].items():
            labels+=f"{prop},"
            if(isinstance(val,int)):
                values+=f"{val},"
            else:
                values+=f"\"{val}\","
        
        # check if the there were any inserted fields
        if(labels[-1]==','):
            query=labels[:-1]+") "+ values[:-1]+")"
        else:
            query=labels+") "+ values+")"
        result  = self.session.execute(query)
        return result
    
    def raw(self,query):
        try:
            result = self.session.execute(query)
        except :
            result = "Error while executing the query"
        return result
    
    # def get_data(args):
    #     return 

    
