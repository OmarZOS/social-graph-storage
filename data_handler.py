



from locator import locator


def handle_data(api,data):
    
    indexer = locator.getIndexer(api)
    for k,values in data:
        print(k)
        print(values)
        if isinstance(values,list):
            for item in values:
                pass
                # indexer.index(doc_type=k,doc_id=[None,item["id"]]("id" in item.keys()),doc_body=item)
                
    
    
    
    



