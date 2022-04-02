
from abc import ABC, abstractmethod

class StorageService(ABC):
    
    @abstractmethod
    def test_connection(api):
        pass
    @abstractmethod
    def saveData(data):
        pass
    @abstractmethod
    def insert_node(data):
        pass
    @abstractmethod
    def insert_edge(data):
        pass
    @abstractmethod
    def queryData(*args):
        pass
