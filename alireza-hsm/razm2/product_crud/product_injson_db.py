import json
from product_inmemory_db import ProductInMemoryDb
from abstraction import ProductSave


class ProductInJsonDb(ProductSave):

    def __init__(self):
        self.product_in_memory = ProductInMemoryDb()
        self.file_path = "./data_file.json" 


    def load_from_json(self) -> dict:
        with open(self.file_path,"r") as file:
            return json.load(file)


    def write_to_json(self):
        with open(self.file_path,"w") as file:
            json.dump(self.data,file,indent=4)


    def add(self,data:dict) -> None:
        self.product_in_memory.add(data)
        self.data = self.product_in_memory.list_all()
        self.write_to_json()
        

    def read_by_title(self,title:str) -> dict:
        instance = self.product_in_memory.read_by_title(title)
        data = self.load_from_json()

        if instance in data:
            return instance
            

    def read(self,product_id:int) -> dict:
        instance = self.product_in_memory.read(product_id)
        read = self.load_from_json()

        if instance in read:
            return instance
        


    def update(self,product_id:int,data_:dict) -> None:
        self.product_in_memory.update(product_id,data_)
        self.data = self.product_in_memory.list_all()
        self.write_to_json()


    def delete(self,product_id:int) -> None:
        self.product_in_memory.delete(product_id)
        self.data = self.product_in_memory.list_all()
        self.write_to_json() 

        

    def list_all(self) -> dict:
        return self.product_in_memory.list_all()