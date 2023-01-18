class Product():
    # ceating list to store all objects
    ـall_objects=[] 

    def __init__(self,category_id:int,title:str,short_description:str,description:str,slug:str,permalink:str,is_available:bool,

                sku:str,price:float,regular_price:float,sale_price:float,manage_stock:int,stock_quantity:int,is_visibla:bool,
        
                date_created_gmt:str,date_modified_gmt:str):
        
        Product.ـall_objects.append(self)
        self.category_id =category_id
        self.title = title
        self.short_description = short_description
        self.description=description
        self.slug = slug
        self.permalik = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visibla = is_visibla
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt

        # category_id check
        assert self.category_id>0,"not valid category_id"

        # price check
        assert self.price>=0 ,"not valid price"
        assert self.sale_price>=0,"not valid price"
        assert self.regular_price>=0,"not valid price"

        # stock check
        assert self.manage_stock>=0 ,"stock can not be empty"
        assert self.stock_quantity>=0,"quantity can not be empty"



    #will read currunt instance
    def read(self) -> str :
        print(self.__repr__())


    #will list(read) all instances
    """i prefer using classmethed expect staticmethod because of preventing 
    from conflict maybe we will have severall class that have same methods 
    """
    @classmethod
    def list_all(cls) -> str :
        for i in Product.ـall_objects:
            print(i.__repr__())


    #update current instance
    def update(self,**kwrgs) -> None :
        for i in kwrgs.keys():
            setattr(self,i,kwrgs[i])

    #update by id
    # i prefer to define this method as classmethod because updating by id does not relevant to specific instance 
    @classmethod
    def update_by_id(cls,id,**kwrgs):
        for i in Product.ـall_objects:
            if i.category_id==id:
                for j in kwrgs.keys():
                    setattr(i,j,kwrgs[j])
                break



    #delete current instance
    def delete(self) -> None :
        #del self
        Product.ـall_objects.remove(self)

    @classmethod
    def delete_all(cls):
        Product.ـall_objects.clear()
        







    def __repr__(self)-> str:
        return f"Product({self.category_id} ,{self.title} ,{self.short_description} ,{self.description} ,{self.slug} ,{self.permalik} ,{self.permalik} ,{self.is_available} ,{self.sku} ,{self.price} ,{self.regular_price} ,{self.sale_price} ,{self.manage_stock} ,{self.stock_quantity} ,{self.is_visibla} ,{self.date_created_gmt} ,{self.date_modified_gmt} )"

    
    def __str__(self) -> str:
        return f"({self.category_id} ,{self.title} ,{self.short_description} ,{self.description} ,{self.slug} ,{self.permalik} ,{self.permalik} ,{self.is_available} ,{self.sku} ,{self.price} ,{self.regular_price} ,{self.sale_price} ,{self.manage_stock} ,{self.stock_quantity} ,{self.is_visibla} ,{self.date_created_gmt} ,{self.date_modified_gmt} )"