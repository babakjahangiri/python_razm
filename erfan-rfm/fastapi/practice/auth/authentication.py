from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database.models import DBUser
from database.db import get_db
from database.hash import Hash
from auth import auth

auth_router = APIRouter(tags=['Authentication'])

@auth_router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.username == request.username).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
        
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid password")
    
    access_token = auth.create_access_token(data={'sub':request.username})
    
    return {
        'access_token':access_token,
        'type_token':'bearer',
        'userID':user.id,
        'username':user.username
    }