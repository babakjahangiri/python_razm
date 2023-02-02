from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from database import user_db 
from database.db import get_db

user_router = APIRouter(tags=['User'], prefix='/user')

@user_router.post('/', response_model=UserDisplay)
def create_user(user: UserBase, db=Depends(get_db)):
    return user_db.create_user(db, user)

# read all users
@user_router.get('/', response_model=list[UserDisplay])
def read_users(db=Depends(get_db)):
    return user_db.get_users(db)

@user_router.get('/{user_id}', response_model=UserDisplay)
def read_user(user_id: int, db=Depends(get_db)):
    user = user_db.get_user(db, user_id)
    if user is not None:
        return user
    else:
        return {"username": "not found", "email": "not found"}
    
@user_router.delete('/{user_id}')
def delete_user(user_id: int, db=Depends(get_db)):
    return user_db.delete_user(db, user_id)

@user_router.post('/update/{user_id}')
def update_user(user_id: int, user: UserBase, db=Depends(get_db)):
    return user_db.update_user(db, user_id, user)