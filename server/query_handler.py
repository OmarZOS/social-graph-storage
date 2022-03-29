
# these functions are responsible for handling search and retrieval queries

from wrappers.REST.http_client import send_data
from wrappers.nebula.nebula_client import nebula_client
from wrappers.nebula.ngqlBuilder import *
# from wrappers.elasticsearch.elastic_client import elastic_wrapper

# elastic = elastic_wrapper()

nebulas = {}

def get_graph_connection(api):
    if(not api in nebulas):
        nebulas[api] = nebula_client(api)
    return nebulas[api]    
    

def handle_search(api,content):
    # TODO: handle advanced search too..
    result = elastic.search(api,content)
    
    return result
    
async def handle_query(api,content,roadmap):
    nebula = get_graph_connection(api)
    ngql_query = ngql_from_struct_filter(api,content)
    result = nebula.raw(ngql_query)
    if(roadmap): # if it has a certain path to follow
        destination = roadmap.pop(0)
        return await send_data(destination,result)
    return result
