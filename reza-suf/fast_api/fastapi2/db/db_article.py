from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle
from fastapi.exceptions import HTTPException
from fastapi import status


def create_article(db: Session, request: ArticleBase):
    article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def read_all_articles(db: Session):
    return db.query(DbArticle).all()


def read_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'not found this {id=}')
    return article


def delete_article(db: Session, id: int):
    db.delete(read_article(db, id))
    db.commit()
    return {"message": "Ok"}


def update_article(db: Session, id: int, request: ArticleBase):
    user = db.query(DbArticle).filter(DbArticle.id == id)
    user.update({
        DbArticle.title: request.title,
        DbArticle.content: request.content,
        DbArticle.published: request.published
    })
    db.commit()
    return {"message": "Ok"}
