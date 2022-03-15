import os
from flask import session
from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config


GRAPH_STORAGE_HOST = str(os.getenv("NEBULA_HOST"))
GRAPH_STORAGE_PORT = int(os.getenv("NEBULA_PORT"))
GRAPH_STORAGE_USER = str(os.getenv("NEBULA_USER"))
GRAPH_STORAGE_PASS = str(os.getenv("NEBULA_PASS"))

class nebula_client(object):
    # define a config
    config = Config()
    config.max_connection_pool_size = 10
    # init connection pool
    connection_pool = ConnectionPool()
    
    # # if the given servers are ok, return true, else return false
    ok = connection_pool.init([('127.0.0.1', 9669)], config)
    
    connection_pool.init([(GRAPH_STORAGE_HOST,GRAPH_STORAGE_PORT)], config)
        
    session = None
    
    def __init__(self,space):
        # get session from the pool
        self.session = self.connection_pool.get_session(GRAPH_STORAGE_USER, GRAPH_STORAGE_PASS)
        # select space
        self.session.execute(f"CREATE SPACE IF NOT EXISTS {space} ( vid_type = INT64 )")
        self.session.execute(f"USE {space}")

    def __del__(self):
        # close the pool
        self.connection_pool.close()
        print("Session ended, farewell nebula..")
    
    def insert(social_network_name,value_type,args):
        try:
            print(0)
        except print(0):
            pass
        
    def raw(self,text):
        result = self.session.execute(text)
        return result
