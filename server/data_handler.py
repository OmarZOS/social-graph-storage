# these functions are responsible for handling insertion queries

from lib2to3.pytree import Base
from grapher.grapher import grapher # should have been installed using pip in a better scenario..
from wrappers.nebula.nebula_client import nebula_client
from wrappers.elasticsearch.elastic_client import elastic_wrapper
from wrappers.neo4j.neo4j_client import Neo4j_client as Neo4j


batch_databases = [Neo4j()]
stream_databases = [nebula_client(),elastic_wrapper()]
    
def handle_data(api,data,roadmap):
    
    # pruning insignificant attributes.. (a legacy issue)
    if("road_map" in data):
        road_map = data.pop("road_map")

    # Neo4j client is a legacy script for which we had no time to work on..
    # THIS IS UNSTABLE!! don't use it in production.
    for db in batch_databases:
        db.insert_nodes(data)
        db.insert_links(data)
        
    # # the recommended insertion is here, uncomment when in deploy mode
    # try:
    #     build_and_insert_graph_from_dict(api,data)
    # except BaseException as e:
    #     print(f"{e}")

    return "Insertion successful.";

def build_and_insert_graph_from_dict(api,data):
    
    try:
        graph = grapher.get_graph(api,data)
    except BaseException as e:
        raise "Error while building graph from data "+str(e)
    # noch nicht
    insert_graph(api,graph)
    
def insert_graph(api,graph):

    for item in graph.nodes(data=True):
        
        # this was a temp entry, it has no place in the schema
        if("node_type" in item[1]):
            tag = item[1].pop("node_type")
        else:
            tag = "unknown"
        for db in stream_databases:
            try:
                db.insert_node(api,tag,item)
            except BaseException as e:
                print (f"Error while inserting a node {e}")
    
    for item in graph.edges(data=True):
        
        # this was a temp entry, it has no place in the schema
        if("edge_type" in item[2]):
            tag = item[2].pop("edge_type")
        else:
            tag = "unknown"
        for db in stream_databases:
            try:
                db.insert_node(api,tag,item)
            except BaseException as e:
                raise "Error while inserting an edge "+str(e)
    
