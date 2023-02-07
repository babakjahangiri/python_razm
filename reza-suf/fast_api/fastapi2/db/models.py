from db.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, index=True, primary_key=True, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String)
    password = Column(String)