from Indexes.indexer import Indexer
from Singleton import singleton
from constants import QUEUES



@singleton
class locator:
    
    indexers = {}
    for api in QUEUES:
        indexers[api] = Indexer(api)
    
    def getIndexer(self,apiname):
        return self.indexers[apiname]



