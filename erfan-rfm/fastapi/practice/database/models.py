from database.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class DBUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    items = relationship('DBArticle', back_populates='user')
    
    
class DBArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('DBUser', back_populates='items')
    published = Column(Boolean, default=False)