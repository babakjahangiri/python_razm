from sqlalchemy.orm import Session
from schemas.product_schemas import ProductSchema
from db.models import Product
from fastapi import HTTPException , status



def product_listall(db:Session):
    try:
        products = db.query(Product).all()
        return products
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)



def product_ById(id:int,db:Session):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        return "Not found"
    else:
        return product
       


def create(db: Session, request: ProductSchema):
    new_product = Product(
        company = request.company,
        name = request.name,
        model = request.model,
        is_available = request.is_available  
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product



def update(request: ProductSchema, id: int, db: Session):
    product = db.query(Product).filter(Product.id == id)
    product.update({
        Product.company : request.company,
        Product.model : request.model,
        Product.name : request.model,
        Product.is_available : request.is_available,
    })
    db.commit()
    return "ok"



def delete(id:int,db:Session):
    product = db.query(Product).filter(Product.id == id).first()
    db.delete(product)
    db.commit()
    return "deleted"