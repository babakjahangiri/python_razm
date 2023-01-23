from product_storage import ProductStorage

class ProductInMemoryDb(ProductStorage):
    __product_list = []

    def __init__(self):
        pass

    def insert(self, product:dict) -> None:
        self.__product_list.append(product)

    def read(self, id:int) -> dict:
        for product in self.__product_list:
            if product['id'] == id:
                return product
        return {}

    def update(self, id:int, attr:dict) -> None:
        for product in self.__product_list:
            if product['id'] == id:
                for key, value in attr.items():
                    if key in product:
                        product[key] = value
                break

    def delete(self, id:int) -> None:
        for product in self.__product_list:
            if product['id'] == id:
                self.__product_list.remove(product)
                break

    def list_all(self) -> list:
        return self.__product_list
