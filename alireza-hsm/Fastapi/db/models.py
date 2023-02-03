from db.databse import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer , String , Boolean


class User(Base):
    __tablename__ = "User"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(Integer)


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer,primary_key=True,index=True)
    company = Column(String)
    name = Column(String)
    model = Column(String)
    is_available = Column(Boolean)