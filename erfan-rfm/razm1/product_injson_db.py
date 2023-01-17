import json
from product_inmemory_db import ProductInMemoryDb
from storage_data import StorageData

class ProductInJsonDb(StorageData):
    
    def __init__(self, path:str="./product_crud/db.json") -> None:
        self.path = path
        self.inmemory_db = ProductInMemoryDb()
        self.data = []
        
        
    def read_json_file(self) -> list:
        try:
            with open(self.path, "r") as json_file:
                return json.load(json_file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
            
    
    def write_json_file(self) -> None:
        try:
            with open(self.path, "w") as json_file:
                json.dump(self.data, json_file, indent=4)
        except (json.JSONDecodeError, FileNotFoundError):
            return None
            
    def find_by_id(self, product_id: int) -> None:
        self.inmemory_db.find_by_id(product_id)
    
    def insert(self, new_product: dict) -> None:
        self.inmemory_db.insert(new_product)
        self.data = self.inmemory_db.list_all()
        self.write_json_file()
        
    def read(self, product_id: int) -> (dict | None):
        return self.inmemory_db.read(product_id)
    
    
    def update(self, product_id: int, updated_data: dict) -> None:
        self.inmemory_db.update(product_id, updated_data)
        self.data = self.inmemory_db.list_all()
        self.write_json_file()
        
        
    def delete(self, product_id: int) -> None:
        self.inmemory_db.delete(product_id)
        self.data = self.inmemory_db.list_all()
        self.write_json_file()
        
        
    def list_all(self) -> list:
        return self.inmemory_db.list_all()