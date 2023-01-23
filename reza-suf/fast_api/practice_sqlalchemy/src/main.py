import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

engine = sqlalchemy.create_engine('sqlite:///database.db')
base = declarative_base()

session = sessionmaker(bind=engine)()


class Student(base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, primary_key=True)
    classroom_id = Column(Integer, ForeignKey("classroom.id"))
    
    
class ClassRoom(base):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    students = relationship('Student', backref='classroomm')
    
    
base.metadata.create_all(engine)


_class = ClassRoom(name='math')
session.add(_class)
# session.commit()

session.add(Student(id=1, name='reza', classroomm=_class))
session.add(Student(id=2, name='mamad', classroomm=_class))
session.add(Student(id=3, name='alireza', classroomm=_class))
session.add(Student(id=4, name='ali', classroomm=_class))

session.commit()

# students = session.query()