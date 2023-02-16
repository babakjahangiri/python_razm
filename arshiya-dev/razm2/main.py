
import datetime
from product import Product
from circle import Circle
import json
import os
from product_inmemory_db import ProductInMemoryDb
from product_injson_db import ProductInJsonDb

def main():
    product_jsonfile = ProductInJsonDb()
    ProductInMemoryDb.loaddata(product_jsonfile.read_from_json())
    # print(os.path.exists('./product_data.json'))
    # print(f"-->{os.path.abspath('.')}")

    mycircle = Circle(8)
    # print(mycircle.__hash__())
    # print(mycircle.area())


    mycircle.radius = 9
    # print(mycircle.__hash__())
    # print(mycircle.area())

    currentdatetime = datetime.datetime.utcnow()
    current_unixtimestamp = int(currentdatetime.timestamp())

    product_one = Product('Lenovo T410s',
        'Lenovo ThinkPad T410s Core i5 M560 2.66GHz 4GB RAM, WIN 10 14" AC ADAPTER',
        'The T410s provides a good companion for office use, that is well suited for business trips thanks to its 14.1 inch size and light weight.',
        'thinkbook-13x-gen-2-(13-inch-intel)',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/thinkbookx/thinkbook-13x-gen-2-(13-inch-intel)/21atcto1wwgb2?cid=gb:sem|se|google|G-UK-SEM-COMMERCIAL-PUBLIC-CCF-LF-Shopping-PLA-Brand-Commercial|Brand-CommercialLaptops-Intel',
        '21ATCTO1WWGB2',
        799.95,
        849.95,
        0,
        False,
        4,
        current_unixtimestamp,
        current_unixtimestamp,
        1)


    product_two = Product('Lenovo T530',
        'Lenovo 530',
        'some long descrition',
        'thinkbook-530',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/530',
        'X394UB83NJ',
        689.95,
        549.95,
        0,
        False,
        8,
        current_unixtimestamp,
        current_unixtimestamp,
        1)

    product_tree = Product('Imack',
        'Lenovo 530',
        'some long descrition',
        'thinkbook-530',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/530',
        'X394UB83NJ',
        689.95,
        549.95,
        0,
        False,
        8,
        current_unixtimestamp,
        current_unixtimestamp,
        1)
 
    #I would like to pass an Id when I create a  new product
   
    product_one.create(1006)

    product_two.create(2001)
    # product_tree.create(1002)
    product_one.title = 'imack'
    product_one.update()
    product_one.id = 888
    product_one.delete()
    print(*ProductInMemoryDb._product_listdb,sep="\n\n")


    # product_one.title = 'Mac book pro 2022'
    # product_one.update()
    # print(Product.delete(1001))
    # print(product_one.list_all())
   
   # print("-------------------------------------")
   # print("Does Product one instance of <<Circle>> class?")
    # print(isinstance(product_one, Circle))
   # print("Does Product one instance of <<Product>> class?")
    # print(isinstance(product_one, Product))


   # del product_one
   # del product_two

   # print(Product.list_all())
      

    #print(Product._product_list)

if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()



