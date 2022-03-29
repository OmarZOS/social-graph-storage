from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config
from constants import *
from locator import singleton
from wrappers.StorageService import StorageService

@singleton
class nebula_client(StorageService):
    


    _get_space_name = lambda self,x : f"{x}_graph"
    
    # define a config
    config.max_connection_pool_size = 10
    config = Config()
    # init connection pool
    connection_pool = ConnectionPool()

    # nebula sessions
    nebulas = {}
    
    def __init__(self,args):
        self.connection_pool.init([(GRAPH_STORAGE_HOST,GRAPH_STORAGE_PORT)], self.config)
    
    def test_connection(self):
        # if the given servers are ok, return true, else return false
        return self.connection_pool.init([(GRAPH_STORAGE_HOST, GRAPH_STORAGE_PORT)], self.config)
        
    def get_nebula_graph_connection(self,api):
        if(not api in self.nebulas):
            # get session from the pool
            self.nebulas[api] = self.connection_pool.get_session(GRAPH_STORAGE_USER, GRAPH_STORAGE_PASS)
            self.init_session(self.nebulas[api],api)
        return self.nebulas[api]

    def init_session(self,session,space):
        
        # select space
        session.execute(f"CREATE SPACE IF NOT EXISTS {self._get_space_name(space)} ( vid_type = INT64 )")
        try:
            session.execute(f"USE {self._get_space_name(space)}")
        except :
            print(f"Can't connect to space: {self._get_space_name(space)} ")
            

    def __del__(self):
        # close the pool
        self.connection_pool.close()
        print("Connection ended, farewell nebula..")
    
    def insert_node(self,social_network_name,tag,node):
        
        session = self.get_nebula_graph_connection(social_network_name)

        labels=f"INSERT VERTEX IF NOT EXISTS {tag}("
        values=f"VALUES {node[0]}:("
        for (prop,val) in node[1].items():
            labels+=f"{prop},"
            if(isinstance(val,int)):
                values+=f"{val},"
            else:
                values+=f"\"{val}\","
            query=labels[:-1]+") "+ values[:-1]+")"
        # check if the there were any inserted fields
        if(labels[-1]==','):
            query=labels[:-1]+") "+ values[:-1]+")"
        else:
            query=labels+") "+ values+")"
        result = session.execute(query)
        return result

    def insert_edge(self,social_network_name,edge_type,edge):

        session = self.get_nebula_graph_connection(social_network_name)

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
        result  = session.execute(query)
        return result
    
    def raw(self,api,query):
        session = self.get_nebula_graph_connection(api)
        try:
            result = session.execute(query)
        except :
            result = "Error while executing the query"
        return result
    
    # def get_data(args):
    #     return 

    
