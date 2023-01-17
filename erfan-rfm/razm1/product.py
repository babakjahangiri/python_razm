from product_inmemory_db import ProductInMemoryDb
from product_injson_db import ProductInJsonDb
from storage_type import StorageType
from datetime import datetime

class Product:

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        self.__id = None
        self.__category_id = category_id
        self.__title = title
        self.__short_description =  short_description
        self.__description = description
        self.__slug = slug
        self.__permalink = permalink
        self.__is_available = is_available
        self.__sku = sku
        self.__price = price
        self.__regular_price = regular_price
        self.__sale_price = sale_price
        self.__manage_stock = manage_stock
        self.__stock_quantity = stock_quantity
        self.__is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt
        self.__db = None
        
    @property
    def id(self):
        return self.__id
    
    @property
    def category_id(self):
        return self.__category_id
    
    @category_id.setter
    def category_id(self, category_id: int):
        if not isinstance(category_id, int):
            raise ValueError('Category Id must be an integer')
        elif category_id < 0:
            raise ValueError('Category Id cannot be less than 0')
        self.__category_id = category_id
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title: str):
        if not isinstance(title, str):
            raise ValueError('Title must be a string')
        self.__title = title
        
    @property
    def short_description(self):
        return self.__short_description
    
    @short_description.setter
    def short_description(self, short_description: str):
        if not isinstance(short_description, str):
            raise ValueError('Short Description must be a string')
        self.__short_description = short_description

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description: str):
        if not isinstance(description, str):
            raise ValueError('Short Description must be a string')
        self.__description = description
        
    @property
    def slug(self):
        return self.__slug
    
    @slug.setter
    def slug(self, slug: str):
        if not isinstance(slug, str):
            raise ValueError('Slug must be a string')
        self.__slug = slug
        
    @property
    def permalink(self):
        return self.__permalink
    
    @permalink.setter
    def permalink(self, permalink: str):
        if not isinstance(permalink, str):
            raise ValueError('Permalink must be a string')
        self.__permalink = permalink
        
    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self, is_available: bool):
        if not isinstance(is_available, bool):
            raise ValueError('Is Available must be a boolean')
        self.__is_available = is_available
        
    @property
    def sku(self):
        return self.__sku
    
    @sku.setter
    def sku(self, sku: str):
        if not isinstance(sku, str):
            raise ValueError('SKU must be a string')
        self.__sku = sku
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price: float):
        if not isinstance(price, float):
            raise ValueError('Price must be a float')
        elif price < 0:
            raise ValueError('Price cannot be less than 0')
        self.__price = price
        
    @property
    def regular_price(self):
        return self.__regular_price
    
    @regular_price.setter
    def regular_price(self, regular_price: float):
        if not isinstance(regular_price, float):
            raise ValueError('Regular Price must be a float')
        elif regular_price < 0:
            raise ValueError('Regular Price cannot be less than 0')
        self.__regular_price = regular_price
        
    @property
    def sale_price(self):
        return self.__sale_price
    
    @sale_price.setter 
    def sale_price(self, sale_price: float):
        if not isinstance(sale_price, float):
            raise ValueError('Sale Price must be a float')
        elif sale_price < 0:
            raise ValueError('Sale Price cannot be less than 0')
        self.__sale_price = sale_price
        
    @property
    def manage_stock(self):
        return self.__manage_stock
    
    @manage_stock.setter
    def manage_stock(self, manage_stock: bool):
        if not isinstance(manage_stock, bool):
            raise ValueError('Manage Stock must be a boolean')
        self.__manage_stock = manage_stock
        
    @property
    def stock_quantity(self):
        return self.__stock_quantity
    
    @stock_quantity.setter
    def stock_quantity(self, stock_quantity: int):
        if not isinstance(stock_quantity, int):
            raise ValueError('Stock Quantity must be an integer')
        elif stock_quantity < 0:
            raise ValueError('Stock Quantity cannot be less than 0')
        self.__stock_quantity = stock_quantity
        
    @property
    def is_visible(self):
        return self.__is_visible
    
    @is_visible.setter
    def is_visible(self, is_visible: bool):
        if not isinstance(is_visible, bool):
            raise ValueError('Is Visible must be a boolean')
        self.__is_visible = is_visible
        
    @property
    def db(self):
        return self.__db
    
    @db.setter
    def db(self, db_type: ProductInJsonDb | ProductInMemoryDb):
        if not isinstance(db_type, (ProductInMemoryDb, ProductInJsonDb)):
            raise ValueError('DB Type must be a ProductInMemoryDb or ProductInJsonDb instance')
        self.__db = db_type

    def create(self, product_id:int, storage_type:str) -> str:
        self.db = StorageType(storage_type).get_db()
        self.__id = product_id
        self.db.insert(
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

    
    def read(self, product_id:int) -> (dict | None):
        return self.db.read(product_id)


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
        
        self.db.update(self.id, data)
        for attr, value in data.items():
            self.__setattr__(attr, value)

    
    def delete(self, product_id) -> None:
            self.db.delete(product_id)


    def list_all(self) -> list:
        return self.db.list_all()


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
       
