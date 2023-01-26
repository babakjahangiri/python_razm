from fastapi import FastAPI
from router import product

def application():
    app = FastAPI()
    app.include_router(product.router)
    return app


app = application()