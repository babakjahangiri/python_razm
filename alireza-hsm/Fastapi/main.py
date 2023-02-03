from fastapi import FastAPI
from router import product
from db.databse import engine
from db import models
from router import user

def application():
    app = FastAPI()
    app.include_router(product.router)
    app.include_router(user.router)
    models.Base.metadata.create_all(engine)
    return app


app = application()