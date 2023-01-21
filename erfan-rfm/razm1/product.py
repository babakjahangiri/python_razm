from datetime import datetime

class Product:
    
    _product_list = []

    _id = 0

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        Product._id += 1
        self.id = Product._id
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
       

    def create(self) -> str:
        self._product_list.append(
            {
                "id" : self.id,
                "category_id" : self.category_id,
                "title" : self.title,
                "short description" : self.short_description,
                "description" : self.description,
                "slug" : self.slug,
                "permalink" : self.permalink,
                "is available" : self.is_available,
                "sku" : self.sku,
                "price" : self.price,
                "regular price" : self.regular_price,
                "sale price" : self.sale_price,
                "manage stock" : self.manage_stock,
                "stock quantity" : self.stock_quantity,
                "is visible" : self.is_visible,
                "date created_gmt" : self.date_created_gmt,
                "date modified gmt" : self.date_modified_gmt
            }
        )
        return self.__repr__()

    #this method shall be able read a product via id/uuid or ... from the product datastructures (dictionary,list or maybe database)
    def read(self, id_:int) -> (dict | None):
        for product in self._product_list:
            if product["id"] == id_:
                return product

    #this method shall be able to update product and amend the data structure for related product
    def update(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, category_id:int = 0, 
                 is_visible = True, is_available:bool = False) -> None:
        currentdatetime = datetime.utcnow()
        current_unixtimestamp = int(currentdatetime.timestamp())

        data = {
                "title":title,
                "short_description":short_description,
                "description":description,
                "slug":slug,"permalink":permalink,
                "sku":sku,
                "price":price,
                "regular_price":regular_price,
                "sale_price":sale_price,
                "manage_stock":manage_stock,
                "stock_quantity":stock_quantity,
                "category_id":category_id,
                "is_visible":is_visible,
                "is_available":is_available,
                "date_modified_gmt":current_unixtimestamp,
               }

        for product in self._product_list:
            if product["id"] == self.id:
                product.update(data)
                for attr, value in data:
                    self.__setattr__(attr, value)
        


    #this method shall be able to remove the product
    @classmethod
    def delete(cls, id_) -> None:
        """Delete product from db by id"""
        for product in cls._product_list:
            if product["id"] == id_:
                cls._product_list.remove(product)


    #shall I get all products with staticmethod ? any better solution ? what about a class method ?
    # what is the difference ?
    # shall I separate the datastructures from the class ? why? who? any better solution?
    @classmethod
    def list_all(cls) -> list:
        return cls._product_list


    def __repr__(self) -> str:
        return f"the product with \n\
        Product Id: {self.id} \n\
        Title: {self.title} \n\
        Short description: {self.short_description} \n\
        Description: {self.description} \n\
        Slug: {self.slug} \n\
        Permanent link: {self.permalink} \n\
        availability: {self.is_available} \n\
        Stock keeping Unit: {self.sku} \n\
        Price: {self.price} \n\
        Regular Price: ${self.regular_price} \n\
        Sale Price: ${self.sale_price} \n\
        Manage Stock {self.manage_stock} \n\
        Stock Quantity: {self.stock_quantity} \n\
        Visible: {self.is_visible} \n\
        Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        "
       