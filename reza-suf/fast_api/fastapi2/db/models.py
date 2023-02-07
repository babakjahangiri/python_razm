from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, index=True, primary_key=True, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String)
    password = Column(String)
    
    
class DbArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, index=True, primary_key=True, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    content = Column(String)
    published = Column(Boolean)
    
    