# these functions are responsible for handling insertion queries

from grapher.grapher import grapher # should have been installed using pip in a better scenario..
from wrappers.nebula.nebula_client import nebula_client
from wrappers.neo4j.neo4j_client import Neo4j_client as Neo4j

# from wrappers.elasticsearch.elastic_client import elastic_wrapper

nebulas = {}
neo4j = Neo4j()

def get_nebula_graph_connection(api):
    if(not api in nebulas):
        nebulas[api] = nebula_client(api)
    return nebulas[api]    
    
def handle_data(api,data,roadmap):
    
    # pruning insignificant attributes.. (a legacy issue)
    if("road_map" in data):
        road_map = data.pop("road_map")

    # Neo4j client is a legacy script for which we had no time to work on..
    # THIS IS UNSTABLE!! don't use it in production.
    neo4j.insert_nodes(data)
    neo4j.insert_links(data)

    # # the recommended insertion is here
    # build_and_insert_graph_from_dict(api,data)

    return "Insertion successful.";

def build_and_insert_graph_from_dict(api,data):
    try:
        graph = grapher.get_graph(api,data)
    except BaseException as e:
        raise "Error while building graph from data "+str(e)
    # noch nicht
    insert_graph(api,graph)
    
def insert_graph(api,graph):
    nebula = get_nebula_graph_connection(api)
    elastic = elastic_wrapper()
    for item in graph.nodes(data=True):
        
        # this was a temp entry, it has no place in the schema
        if("node_type" in item[1]):
            tag = item[1].pop("node_type")
        else:
            tag = "unbekannt"
        try:
            nebula.insert_node(api,tag,item)
            elastic.insert_node(api,tag,item)
        except BaseException as e:
            raise "Error while inserting a node "+str(e)
    
        
    for item in graph.edges(data=True):
        
        # this was a temp entry, it has no place in the schema
        if("edge_type" in item[2]):
            tag = item[2].pop("edge_type")
        else:
            tag = "unbekannt"
        try:
            nebula.insert_edge(api,tag,item)
            elastic.insert_edge(api,tag,item)
        except BaseException as e:
            raise "Error while inserting an edge "+str(e)
    
