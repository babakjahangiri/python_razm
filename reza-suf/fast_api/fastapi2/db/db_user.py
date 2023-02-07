from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser

def create_user(db:Session, request:UserBase):
    user = DbUser(
        username = request.username,
        email = request.email,
        password = request.password
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def read_all_users(db:Session):
    return db.query(DbUser).all()


def read_user(db:Session, id:int):
    return db.query(DbUser).filter(DbUser.id == id).first()
    
    
def delete_user(db:Session, id:int):
    db.delete(read_user(db, id))
    db.commit()
    return {"message":"Ok"}


def update_user(db:Session, id:int, request:UserBase):
    user = db.query(DbUser).filter(DbUser.id==id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: request.password
    })
    db.commit()
    return {"message":"Ok"}
