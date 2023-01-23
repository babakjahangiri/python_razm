from abc import ABC, abstractmethod


class ProductStorage(ABC):
    
    @abstractmethod
    def insert(self, product:dict):
        pass
    
    @abstarctmethod
    def read(self, id:int):
        pass
    
    @abstarctmethod
    def delete(self, id:int):
        pass
    
    @abstractmethod
    def update(self, id:int, attr:dict):
        pass
    
    @abstarctmethod
    def list_all(self):
        pass

