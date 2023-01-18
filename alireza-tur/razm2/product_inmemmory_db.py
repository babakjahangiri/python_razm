class ProductInMemoryDb:
    _product_list = []

    @classmethod
    def insert(cls,dic:dict) -> int :
        try:
            ProductInMemoryDb._product_list.append(dic)
            return 1
        except:
            print("failed")
            return -1

    @classmethod
    def read(cls,id:int) -> str:
        for i in ProductInMemoryDb._product_list :
            if i['id']==id:
                return i
        else:
            return "object not fount"



    @classmethod
    def read_all(cls) -> None :
        for i in  ProductInMemoryDb._product_list:
            print(i)


    @classmethod
    def update(cls,id:int,dic:dict) -> int :
        for i in ProductInMemoryDb._product_list :
            if i['id']==id:
                ProductInMemoryDb._product_list.remove(i)
                ProductInMemoryDb._product_list.append(dic)
                print("update successfull")
                return 1

        else:
            print("update unsuccessfull")
            return -1

    

    

    @classmethod
    def delete(cls,id:int) -> int :
        
        for i in ProductInMemoryDb._product_list :
                if i['id']==id:
                    ProductInMemoryDb._product_list.remove(i)
                    print("delete successful")
                    return 1

        else:
            print("delete unsuccesful")
            return -1


    @classmethod
    def delete_all(cls) -> str :
        ProductInMemoryDb._product_list.clear()
        return "delete all succesful"
