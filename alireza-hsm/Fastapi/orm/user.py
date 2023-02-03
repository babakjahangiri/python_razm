from schemas.user_schema import UserSchema
from sqlalchemy.orm import Session
from db.models import User



def user_listall(db: Session):
    user = db.query(User).all()
    return user





def create_user(db: Session, request: UserSchema):
    new_user = User(
        username = request.username,
        email = request.email,
        password = request.password,
    ) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user