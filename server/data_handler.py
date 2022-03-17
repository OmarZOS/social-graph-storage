# from locator import locator

from wrappers.nebula.nebula_client import nebula_client

from grapher.grapher import grapher # should have been installed using pip in a better scenario..
# from wrappers.elasticsearch.elastic_client import elastic_wrapper

def handle_data(api,data,destination):
    
    # pruning insignificant attributes..
    if(data["road_map"]):
        road_map = data.pop("road_map")
    
    graph = grapher.get_graph(api,data)
    
    nebula = nebula_client(api)

    # noch nicht
    # elastic = elastic_wrapper(api)
    
    for item in graph.nodes(data=True):
        
        # this was a temp entry, it has no place in the schema
        tag = item[1].pop("other")
        nebula.insert_node(api,tag,item)
        # elastic.insert()
        
    for item in graph.edges(data=True):
        
        # this was a temp entry, it has no place in the schema
        tag = item[2].pop("other")
        nebula.insert_edge(api,tag,item)
        # elastic.insert()
    
