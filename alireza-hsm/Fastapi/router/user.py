from fastapi import APIRouter , Depends
from schemas.user_schema import UserSchema
from db.databse import get_db
from orm import user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user",tags=["User"])

# add
@router.post("/add")
def create(request: UserSchema, db:Session = Depends(get_db)):
    return user.create_user(db,request)

# list all
@router.get("/retrieve")
def list_all(db: Session = Depends(get_db)):
    return user.user_listall(db)

# update


# read 


# delete