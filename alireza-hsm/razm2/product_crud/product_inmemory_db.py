from abstraction import ProductSave

class ProductInMemoryDb(ProductSave):
    __product_list = []

    def __init__(self):
        pass
    
    def add(self,data:dict) -> list:
        self.__product_list.append(data)

    
    def read_by_title(self,title:str) -> dict:
        for item in self.__product_list:
            if item["title"] == title:
                return item

    

    def read(self,product_id:int) -> dict:
            for item in self.__product_list:
                if item["id"] == product_id:
                    return item



    def update(self,product_id:int,data:dict) -> None:
        for item in self.__product_list:
            if item["id"] == product_id:
                item.update(data)
                break
                
    

    def delete(self,product_id:int) -> None:
        for item in self.__product_list:
            if item["id"] == product_id:
                self.__product_list.remove(item)
                break

        
    def list_all(self) -> list:
        return self.__product_list