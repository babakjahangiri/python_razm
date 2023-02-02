from sqlalchemy.orm import Session
from schemas import ArticleBase
from database.models import DBArticle
from fastapi.exceptions import HTTPException
from fastapi import status

def create_article(db: Session, request: ArticleBase):
    db_article = DBArticle(
            title=request.title,
            content=request.content,
            user_id=request.creator_id,
            published=request.published,
        )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles(db: Session):
    return db.query(DBArticle).all()


def get_article(db: Session, article_id: int):
    article = db.query(DBArticle).filter(DBArticle.id == article_id).first()
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"article with id {article_id} not found")
    return article

def delete_article(db: Session, article_id: int):
    article = get_article(db, article_id)
    db.delete(article)
    db.commit()
    return {"message": "article deleted"}

def update_article(db: Session, article_id: int, request: ArticleBase):
    db.query(DBArticle).filter(DBArticle.id == article_id).update({
        DBArticle.title: request.title,
        DBArticle.content: request.content,
        DBArticle.user_id: request.creator_id,
        DBArticle.published: request.published
    })
    db.commit()
    return {"message": "article updated"}
