
import json
import networkx as nx
from networkx.readwrite import json_graph

def read_json_file(filename):
    with open(filename) as f:
        js_graph = json.load(f)
    return json_graph.node_link_graph(js_graph)
# with open("databases-config/nebula/schemas/twitter.json") as f :
#     schema = json.load(f)

net = "linkedIn"

graph = read_json_file(f"databases-config/nebula/schemas/{net}.json")

print(f"CREATE SPACE IF NOT EXISTS {net}_graph ( vid_type = INT64 );")
print(f"USE {net}_graph;")

for node in graph.nodes(data=True):
    # print(node)
    for (key,values) in node[1].items():
        instruction = "CREATE TAG IF NOT EXISTS {}(".format(key)
        for item in values:
            for (k,v) in item.items():
                instruction += "{} {},".format(k,v)
        
    if(instruction[-1] == ","):
        print(instruction[:-1]+");") # [:-1] to remove the last comma, supposing that there are no empty items in the schema 
    else:
        print(instruction+");")
    
for (key1,key2,values) in graph.edges(data=True):
    for (kk,vv) in values.items():
        # print(vv)
        instruction = "CREATE EDGE IF NOT EXISTS {}(".format(kk)
        
        for item in vv:
            for (k,v) in item.items():
                instruction += "{} {},".format(k,v)
    
    if(instruction[-1] == ","):
        print(instruction[:-1]+");") # [:-1] to remove the last comma, supposing that there are no empty items in the schema 
    else:
        print(instruction+");")
