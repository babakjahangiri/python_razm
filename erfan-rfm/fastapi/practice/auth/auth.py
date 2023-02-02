from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import timedelta, datetime
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import DBUser

oauth_schema = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = '53ab4f1f78fd32923dc0dee2bd9613294e6001db130833f5347b17fc003d174e'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expire_delta: timedelta | None = None):
    to_encode = data.copy()
    if expire_delta is not None:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth_schema), db: Session = Depends(get_db)):
    error_credentials = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid credentials', headers={'WWW-authenticate':'bearer'})
    
    try:
        _dict = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username = _dict.get('sub')
        if username is None:
            raise error_credentials
    except JWTError:
        raise error_credentials
    
    user = db.query(DBUser).filter(DBUser.username == username).first()
    
    return user
        