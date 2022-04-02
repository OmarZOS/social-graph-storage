import json
from networkx.readwrite import json_graph

# this class returns a graph of data, no matter the format..
class grapher(object):
    
    @staticmethod
    def get_graph(api,data):
        # should be more sophisticated, but still..
        return grapher.from_networkx(data)
    
    @staticmethod
    def from_networkx(data):
        graph = json_graph.node_link_graph(data)
        # -------------Playground---------------
        
        # for item in graph.nodes(data=True):
        #     if "node_type" not in item[1]:
        #         print(item)
        
        # # # for edge in graph.edges(data=True):
        # # #     tag=edge[2].pop("other")
        # # #     # for (k1,k2,v) in item.items():
        # # #     # print(f"{k1[0]}")
        # # #     labels=f"INSERT EDGE IF NOT EXISTS follow("
        # # #     values=f"VALUES {edge[0]} -> {edge[1]}:("
        # # #     for (prop,val) in edge[2].items():
        # # #         labels+=f"{prop},"
        # # #         if(isinstance(val,int)):
        # # #             values+=f"{val},"
        # # #         else:
        # # #             values+=f"\"{val}\","
            
        # # #     # check if the there were any inserted fields
        # # #     if(labels[-1]==','):
        # # #         query=labels[:-1]+") "+ values[:-1]+")"
        # # #     else:
        # # #         query=labels+") "+ values+")"
        # # #     print(query)
            
            # for (prop,data) in v.items():
            #     print(f"{prop}:{data}")
            
        # --------------------------------------
        return graph
    
    
if __name__=="__main__":
    with open("graphe") as f:
        graph  = json.load(f)
    grapher.from_networkx(graph)