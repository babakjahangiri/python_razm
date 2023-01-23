import json
from product_storage import ProductStorage


class ProductInJsonDb(ProductStorage):
    flag = False

    def __init__(self) -> None:
        if not self.flag:
            self.flag = True
            with open("products.json", "w") as f:
                json.dump([], f)

    def __read_file(self) -> list:
        with open("products.json", "r") as f:
            return json.load(f)

    def insert(self, product:dict) -> None:
        products = ProductInJsonDb.__read_file()
        products.append(product)
        with open("products.json", "w") as f:
            json.dump(products, f, indent=4)

    def read(self, id:int) -> dict:
        products = ProductInJsonDb.__read_file()
        for product in products:
            if product['id'] == id:
                return product
        return {}

    def update(self, id:int, attr:dict) -> None:
        products = ProductInJsonDb.__read_file()
        for product in products:
            if product['id'] == id:
                for key, value in attr.items():
                    if key in product:
                        product[key] = value
                break
        with open("products.json", "w") as f:
            json.dump(products, f, indent=4)

    def delete(self, id:int) -> None:
        products = ProductInJsonDb.__read_file()
        for product in products:
            if product["id"] == id:
                products.remove(product)
                break
        with open("product.json", "r") as f:
            json.dump(products, f, indent=4)

    def list_all(self) -> list:
        products = ProductInJsonDb.__read_file()
        return products
