import re

from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from database.hash import Hash
from database.models import DBUser
from schemas import UserBase
from exceptions import EmailNotValidError

def validate_email(email):
  regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
  if(re.search(regex, email)):  
    return True  
  else:  
    return False


def create_user(db: Session, request: UserBase):
    if not validate_email(request.email):
        raise EmailNotValidError("invalid email")
    
    db_user = DBUser(
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password)
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(DBUser).all()


def get_user(db: Session, user_id: int):
    return db.query(DBUser).filter(DBUser.id == user_id).first()

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()
    return {"message": "user deleted"}

def update_user(db: Session, user_id: int, request: UserBase):
    db.query(DBUser).filter(DBUser.id == user_id).update({
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return {"message": "user updated"}
