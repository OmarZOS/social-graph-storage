from locator import locator

from wrappers.nebula.nebula_client import nebula_client
from Indexes.indexer import Indexer

def handle_data(api,data):
    
    indexer = Indexer(api)
    
    for (k,values) in data.items():
        print("received dateien..")
        pass
        # if isinstance(values,list):
        #     # print(values)
        #     for item in values:
        #         if "id" in item.keys() or "other" in item.keys():
        #             _doc_id = ["other","id"]("id" in item.keys())
        #             indexer.index(doc_type=k,doc_id=str(_doc_id),doc_body=item)
        #     #     pass
                
    
    
    
    



