from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from database.db import engine
from database.models import Base
from exceptions import EmailNotValidError
from routers.article import article_router
from routers.user import user_router
from routers.product import product_router
from auth.authentication import auth_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(article_router)
app.include_router(product_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.exception_handler(EmailNotValidError)
def email_not_valid_handler(request: Request, exc: EmailNotValidError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=str(exc),
    )