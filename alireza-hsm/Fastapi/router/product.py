from fastapi import APIRouter , Depends
from db.databse import get_db
from sqlalchemy.orm import Session
from schemas.product_schemas import ProductSchema
from orm import product as productfile
from orm.product import product_listall , product_ById , update , delete

router = APIRouter(prefix="/product",tags=["Product"])


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return product_listall(db)


@router.get("/{id}/")
def product(id: int, db: Session = Depends(get_db)):
   return product_ById(id,db)


@router.post("/create")
def create_product(request: ProductSchema, db: Session = Depends(get_db)):
    return productfile.create(db,request)


@router.put("/update/{id}")
def update_product(request: ProductSchema, id: int, db: Session = Depends(get_db)):
    return update(request,id,db)


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    return delete(id,db)