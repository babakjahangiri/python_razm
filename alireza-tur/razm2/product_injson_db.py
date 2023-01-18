import json
#borrow object list from ProductInMemoryDb not right way but i still try to find solution
from product_inmemmory_db import ProductInMemoryDb


class ProductInJasonDb:

    #private method
    def __read_json() -> dict:
        with open('product.json', 'r') as js:
            data = json.load(js)
        return data

    #private method
    def __write_to_json(dic:dict) -> None:
        with open("product.json", "w") as js:
                ProductInMemoryDb._product_list.append(dic)
                json.dump( ProductInMemoryDb._product_list,js,indent=4)
    
    #private method
    def __rewrite_to_json() -> None:
        with open("product.json", "w") as js:
            json.dump( ProductInMemoryDb._product_list,js,indent=4)
        

    @classmethod
    def insert(cls,dic:dict) -> int :
        try:
            ProductInJasonDb.__write_to_json(dic)
            print("insert successful")
            return 1
    
        except:
            print("failed")
            return -1


    @classmethod
    def read(cls,id:int) -> str:
        for i in ProductInJasonDb.__read_json() :
            if i['id']==id:
                return i
        else:
            return "object not fount"


    @classmethod
    def read_all(cls) -> None :
        for i in  ProductInJasonDb.__read_json():
            print(i)



    @classmethod
    def update(cls ,id:int ,dic:dict ) -> int :
            for i in ProductInJasonDb.__read_json() :
                if i['id']==id:
                    ProductInJasonDb.__write_to_json(dic)
                print("update successful")
                return 1

            else :
                print("update unsuccessfull")
                return -1


    @classmethod
    def delete(cls,id:int) -> int :
        for i in ProductInJasonDb.__read_json() :
            if i['id']==id:
                ProductInMemoryDb._product_list.remove(i)
                ProductInJasonDb.__rewrite_to_json()
                print("delete successful")
                return 1
        else:
            print("delete unsuccesful")
            return -1


    @classmethod
    def delete_all(cls) -> str :
        ProductInMemoryDb._product_list.clear()
        ProductInJasonDb.__rewrite_to_json()
        print("delete all succesful")
        return "delete all succesful"





