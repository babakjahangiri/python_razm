from fastapi import FastAPI
from router import blog_get, blog_post, user, article
from db import models
from db.database import engine
from exceptions import EmailNotValid
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
models.Base.metadata.create_all(engine)


@app.get('/')
async def hello():
    return "hello from Route!"


@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request, exc: EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)
