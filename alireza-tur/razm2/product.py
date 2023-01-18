from abc import ABC,abstractclassmethod
from datetime import datetime
from product_injson_db import ProductInJasonDb as js
from product_inmemmory_db import ProductInMemoryDb as mm

class Product():
    _all=[]

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        self.id = None
        self.category_id = category_id
        self.title = title
        self.short_description =  short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt
        
        


    def info(self) -> dict :
        self.inf={"id":self.id,"category_id":self.category_id,"title":self.title,"short_description":self.short_description
        ,"slug":self.slug,"permalink":self.permalink,"is_available":self.is_available,"sku":self.sku,"price":self.price,"regular_price":self.regular_price
        ,"sale_price":self.sale_price,"manage_stock":self.manage_stock,"stock_quantity":self.stock_quantity,"is_visible":self.is_visible
        ,"date_created_gmt":self.date_created_gmt,"date_modified_gmt":self.date_modified_gmt}

        return self.inf


    def create(self,id:int) -> dict :
        self.id=id
        self.first_info={"id":self.id,"category_id":self.category_id,"title":self.title,"short_description":self.short_description
        ,"slug":self.slug,"permalink":self.permalink,"is_available":self.is_available,"sku":self.sku,"price":self.price,"regular_price":self.regular_price
        ,"sale_price":self.sale_price,"manage_stock":self.manage_stock,"stock_quantity":self.stock_quantity,"is_visible":self.is_visible
        ,"date_created_gmt":self.date_created_gmt,"date_modified_gmt":self.date_modified_gmt}



    
    def __str__(self) -> str:
        return f'{{\
            "id": "{self.id}",\n\
            "title": "{self.title}",\n\
            "short_description": "{self.short_description}",\n\
            "description": "{self.description}",\n\
            "slug": "{self.slug}",\n\
            "permalink": "{self.permalink}", \n\
            "is_available": "{self.is_available}",\n\
            "sku": "{self.sku}",\n\
            "Price": "{self.price}",\n\
            "regular_price": "{self.regular_price}", \n\
            "sale_price": "{self.sale_price}", \n\
            "manage_stock" "{self.manage_stock}", \n\
            "stock_quantity": "{self.stock_quantity}", \n\
            "is_visible": "{self.is_visible}", \n\
            "date_created_gmt": "{self.date_created_gmt}", \n\
            "date_modified_gmt": "{self.date_modified_gmt}", \n\
            }}'
        


    def __repr__(self) -> str :
        return f"the product with \n\
        Product Id: {self.id} \n\
        Title: {self.title} \n\
        Short description: {self.short_description} \n\
        Description: {self.description} \n\
        Slug: {self.slug} \n\
        Permanent link: {self.permalink} \n\
        availablity: {self.is_available} \n\
        Stock keeping Unit: {self.sku} \n\
        Price: {self.price} \n\
        Reqular Price: ${self.regular_price} \n\
        Sale Price: ${self.sale_price} \n\
        Manage Stock {self.manage_stock} \n\
        Stock Quantity: {self.stock_quantity} \n\
        Visible: {self.is_visible} \n\
        Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        "    
    


# open/close principle
class ProductStorage(ABC):
    @abstractclassmethod
    def insert(dic:dict):
        pass

    @abstractclassmethod
    def read(id:int):
        pass

    @abstractclassmethod
    def read_all():
        pass

    @abstractclassmethod
    def update(id:int,dic:dict):
        pass

    @abstractclassmethod
    def delete(id:int):
        pass
        
    @abstractclassmethod
    def delete_all():
        pass



class SaveInMemory(ProductStorage):
    # inmmemory methods
    # crud
    def insert(dic:dict):
        mm.insert(dic)

    def read(id:int):
        mm.read(id)

    def read_all():
        mm.read_all()    

    def update(id:int,dic:dict):
        mm.update(id,dic)

    def delete(id:int):
        mm.delete(id)
        
    def delete_all():
        mm.delete_all()


class SaveInJson(ProductStorage):
    # injson methods
    # crud
    def insert(dic:dict):
        js.insert(dic)

    def read(id:int):
        js.read(id)

    def read_all():
        js.read_all()

    def update(id:int,dic:dict):
        js.update(id,dic)
        
    def delete(id:int):
        js.delete(id)
        
    def delete_all():
        js.delete_all()


