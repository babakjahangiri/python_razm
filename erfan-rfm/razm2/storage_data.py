from abc import ABC, abstractmethod

class StorageData(ABC):
    
    @abstractmethod
    def insert(self, new_product:dict) -> None:
        pass

    @abstractmethod
    def update(self, product_id:int, updated_data:dict):
        pass

    @abstractmethod
    def delete(self, product_id:int)-> None:
        pass

    @abstractmethod
    def read(self, product_id:int)-> None:
        pass

    @abstractmethod
    def find_by_id(self, product_id:int) -> None:
        pass

    @abstractmethod
    def list_all(self)-> None:
        pass    
