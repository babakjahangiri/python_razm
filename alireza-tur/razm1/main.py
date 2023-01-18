from product import Product
item1=Product(1,"iphone 12 mini","phone","apple mobile phone","iphone-12","https://www.apple.com/shop/buy-iphone/iphone-12",True,"A2176",600,600,799,20,20,True,"2022/12/15","2022/12/20")


print(item1) # __str__
print(Product.ـall_objects)#__repr__

Product.update_by_id(1,title="iphone 13") # will set item1 title to iphone 13



class Car():
    def __init__(self,name:str,company:str,price:float,year:int):
        self.name=name
        self.company=company
        self.price=price
        self.year=year

    def __reper__(self):
        return f"Car({self.name}, {self.company} ,{self.price} ,{self.year})"

car1=Car("cls","Benz",1000000,2019)


#type 

print(type(Product)) # <class 'type'>
print(type(Car)) # <class 'type'>
print(type(item1))#<class 'product.Product'>  -- because class is in an other file 
print(type(car1))#<class '__main__.Car'>


#isinstance
# The isinstance() function returns True if the specified object is of the specified type, otherwise False
print(isinstance(car1,Product)) #False
print(isinstance(car1,Car)) #True