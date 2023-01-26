from fastapi import APIRouter , status , Response
from pydantic import BaseModel

router = APIRouter(prefix="/product",tags=["Product"])

class Product(BaseModel):
    name: str
    quantity : int = 0
    category: str


@router.get("/")
def list_all():
    return {"message":"products"}


@router.get("/{product_id}")
def product(product_id:int,response:Response):
    if product_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error":"not found"}
    response.status_code = status.HTTP_200_OK
    return {"message": product_id}



@router.post("/create")
def create_product(info:Product,number: int | None = None):
    return {"message":f"product with {info} added.{number}"}


@router.post("/update/{product_id}",
            description="You can Update Api with product id",
            summary= "Done",
            response_description="#"
            )
def update_product(product_id:int):
    return {"message":f"product with id {product_id} updated."}



@router.delete("/{product_id}")
def delete_product(product_id):
    return {"message":f"product with id {product_id} deleted."}