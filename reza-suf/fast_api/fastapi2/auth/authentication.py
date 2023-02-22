from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from db.database import get_db
from db import models
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.hash import Hash
from auth import oauth2

router = APIRouter(tags=['authentication'])


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(
        request.username == models.DbUser.username).first()

    if not user:
        raise HTTPException(status_code=404, detail="invalid credential")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail="invalid password")

    access_token = oauth2.create_access_token(data={'sub': request.username})

    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userID': user.id,
        'username': user.username
    }
