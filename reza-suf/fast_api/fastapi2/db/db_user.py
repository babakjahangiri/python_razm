from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from fastapi.exceptions import HTTPException
from fastapi import status
from exceptions import EmailNotValid


def create_user(db: Session, request: UserBase):
    if '@' not in request.email:
        raise EmailNotValid('Email not valid')
    user = DbUser(
        username=request.username,
        email=request.email,
        password=request.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(id, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'not found this {id=}')
    return user


def delete_user(id, db: Session):
    user = get_user(id, db)
    db.delete(user)
    db.commit()
    return 'ok'


def update_user(id, db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password),
    })
    db.commit()
    return 'ok'
