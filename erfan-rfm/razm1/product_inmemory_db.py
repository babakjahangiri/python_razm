from storage_data import StorageData

class ProductInMemoryDb(StorageData):
    __product_list = []
    
    @staticmethod
    def load_data(data: list):
        ProductInMemoryDb.__product_list.extend(data)
    
    def find_by_id(self, product_id:int) -> bool:
        for product_dict in self.__product_list:
            if product_dict["id"] == product_id:
                return True
        return False
    
    def insert(self, new_product:dict) -> None:
        self.__product_list.append(new_product)
        
    def read(self, product_id:int) -> (dict | None):
        if self.find_by_id(product_id):
            for product in self.__product_list:
                if product["id"] == product_id:
                    return product
        return None
    
    def update(self, product_id:int, updated_data:dict) -> None:
        if self.find_by_id(product_id):
            for product in self.__product_list:
                if product["id"] == product_id:
                    product.update(updated_data)        
        

    def delete(self, product_id:int) -> None:
        if self.find_by_id(product_id):
            for product in self.__product_list:
                if product["id"] == product_id:
                    self.__product_list.remove(product)
            
    @classmethod
    def list_all(cls) -> list:
        return cls.__product_list
