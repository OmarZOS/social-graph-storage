
# these functions are responsible for handling search and retrieval queries

from wrappers.REST.http_client import send_data
from wrappers.nebula.nebula_client import nebula_client
from wrappers.nebula.ngqlBuilder import *
from wrappers.elasticsearch.elastic_client import elastic_wrapper

elastic = elastic_wrapper()

# nebulas = {}
# gdb = nebula_client()
    
tags=[]


def handle_search(api,content):

    # TODO: handle advanced search too..
    searchBody = {
        "simple_query_string": {
            # "_source":f"{api}",
            "query": f"{content}\"",
            # "fields": ["fulltext", "title^5", "name^10"]
        }
    }
    
    # {"query": {
    #     "match": {
    #     "text": {"query":content}
    # }
    # }
    # }
        
    return elastic.search(api,searchBody)
    
    
async def handle_query(api,content,roadmap):
    nebula = get_graph_connection(api)
    ngql_query = ngql_from_struct_filter(api,content)
    result = nebula.raw(ngql_query)
    if(roadmap): # if it has a certain path to follow
        destination = roadmap.pop(0)
        return await send_data(destination,result)
    return result
