from fastapi import APIRouter, Response, Header, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from database.db import get_db


product_router = APIRouter(tags=['Product'], prefix='/product')

products = [
    "product1",
    "product2",
    "product3"
]

@product_router.get('/')
def get_all():
    data = ' '.join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key='mycookie', value='cookie_value')
    return response

@product_router.get('/{id}', responses={
    404:{"content":{"text/plain":{"example":"product not found!"}}, "description":"no product found"},
    200:{"content":{"text/html":{"example":"<div> product </div>"}}, "description":"Html format"}
})
def get_single(id: int):
    if id > len(products)-1:
        return PlainTextResponse(content="not found", status_code=404)
    data = products[id]
    return HTMLResponse(content=f"<div> {data} </div>")

# recieve and send headers
@product_router.get('/{id}/json', response_model=str, responses={ 200:{"content":{"application/json":{"example":"{'product':'product1'}"}}, "description":"Json format"} })     
def get_single_json(id: int, response: Response, x_custom: list[str] = Header(None), mycookie: str = Cookie(None)):
    if id > len(products)-1:
        response.status_code = 404
        return "not found"
    data = products[id]
    print(mycookie)
    return JSONResponse(content={"product": data, "header": x_custom, 'coockies':mycookie})


@product_router.post('/create')
def create_products(data: str = Form(...)):
    products.append(data)
    return products