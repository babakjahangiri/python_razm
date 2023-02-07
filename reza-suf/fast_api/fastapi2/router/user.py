from fastapi import APIRouter, status, Response, Query, Body, Path, Depends
from typing import Optional, List
from pydantic import BaseModel
from schemas import UserBase, UserDisplay 
from db import db_user
from db.database import get_db

router = APIRouter(prefix='/user', tags=['user'])


# create user
@router.post('/', response_model=UserDisplay)
def create_user(user:UserBase, db=Depends(get_db)):
    return db_user.create_user(db, user)


# read All user 
@router.get('/', response_model=List[UserDisplay])
def read_all_users(db=Depends(get_db)):
    return db_user.read_all_users(db)


# read user
@router.get('/{id}', response_model=UserDisplay)
def read_user(id:int, db=Depends(get_db)):
    return db_user.read_user(db, id)


# update user
@router.post('/update/{id}')
def update_user(id:int, user:UserBase, db=Depends(get_db)):
    return db_user.update_user(db, id, user)


# delete user
@router.get('/delete/{id}')
def delete_user(id:int, db=Depends(get_db)):
    return db_user.delete_user(db, id)
