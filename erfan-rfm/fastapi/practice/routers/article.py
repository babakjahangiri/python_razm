from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from database import article_db 
from database.db import get_db
from auth.auth import get_current_user
from schemas import UserBase
article_router = APIRouter(tags=['Article'], prefix='/article')



@article_router.post('/', response_model=ArticleDisplay)
def create_article(article: ArticleBase, db=Depends(get_db)):
    return article_db.create_article(db, article)



# read all articles
@article_router.get('/', response_model=list[ArticleDisplay])
def read_articles(db=Depends(get_db)):
    return article_db.get_articles(db)



@article_router.get('/{article_id}')
def read_article(article_id: int, db=Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data':article_db.get_article(db, article_id),
        'current_user':current_user
    }
    
    
    
    
@article_router.delete('/{article_id}')
def delete_article(article_id: int, db=Depends(get_db)):
    return article_db.delete_article(db, article_id)



@article_router.post('/update/{article_id}')
def update_article(article_id: int, article: ArticleBase, db=Depends(get_db)):
    return article_db.update_article(db, article_id, article)