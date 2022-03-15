
import json

with open("databases/nebula/schemas/twitter.json") as f :
    schema = json.load(f)

print("CREATE SPACE IF NOT EXISTS {}_graph;".format("twitter"))
print("USE SPACE {}_graph;".format("twitter"))

for (key,values) in schema.items():
    instruction = "CREATE TAG IF NOT EXISTS {}(".format(key)
    for item in values:
        for (k,v) in item.items():
            instruction += "{} {},".format(k,v)
        
    print(instruction[:-1]+");") # [:-1] to remove the last comma, supposing that there are no empty items in the schema 
    