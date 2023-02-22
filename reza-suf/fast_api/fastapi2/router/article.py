from fastapi import APIRouter, status, Response, Query, Body, Path, Depends
from typing import Optional, List
from pydantic import BaseModel
from schemas import ArticleBase, ArticleDisplay, UserBase
from db import db_article
from db.database import get_db
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/article', tags=['article'])


# create article
@router.post('/', response_model=ArticleDisplay)
def create_article(user: ArticleBase, db=Depends(get_db)):
    return db_article.create_article(db, user)


# read All article
@router.get('/', response_model=List[ArticleDisplay])
def read_all_articles(db=Depends(get_db)):
    return db_article.read_all_articles(db)


# read article
@router.get('/{id}', response_model=ArticleDisplay)
def read_article(id: int, db=Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    # return db_article.read_article(db, id)
    return {
        "data": db_article.read_article(db, id),
        "current_user": current_user
    }


# update article
@router.post('/update/{id}')
def update_article(id: int, article: ArticleBase, db=Depends(get_db)):
    return db_article.update_article(db, id, article)


# delete article
@router.get('/delete/{id}')
def delete_article(id: int, db=Depends(get_db)):
    return db_article.delete_article(db, id)
