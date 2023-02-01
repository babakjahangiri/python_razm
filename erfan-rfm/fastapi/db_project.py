from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


class DB:
    _engin = create_engine("sqlite:///project.db")
    _base = declarative_base()
    
    def __init__(self) -> None:
        self.session = sessionmaker(bind=self._engin)()
        
    def create_all_tables(self):
        self._base.metadata.create_all(self._engin)
        
    class Model:
        id = Column("id", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
        
    class Major(Model, _base):
        __tablename__ = "major"
        name = Column("name", String(50))
        students = relationship("Student", backref="major")
        classes = relationship("Class", backref="major")
        
    class Teacher(Model, _base):
        __tablename__ = "teacher"
        name = Column("name", String(50))
        family = Column("family", String(50))
        class_ = relationship("Class", backref="teacher")
        
    class Student(Model, _base):
        __tablename__ = "student"
        name = Column("name", String(50))
        family = Column("family", String(50))
        major_id = Column("major_id", Integer, ForeignKey("major.id"))
        
    class Class(Model, _base):
        __tablename__ = "class"
        name = Column("name", String(50))
        teacher_id = Column("teacher_id", Integer, ForeignKey("teacher.id"))
        major_id = Column("major_id", Integer, ForeignKey("major.id"))

        
        
# test case
if __name__ == "__main__":
    db = DB()
    db.create_all_tables()

    # create major
    major = DB.Major(name="computer")
    db.session.add(major)
    db.session.commit()
    
    # create teacher
    teacher = DB.Teacher(name="hosein", family="hoseini")
    db.session.add(teacher)
    db.session.commit()
    
    # create class
    class_ = DB.Class(name="python", teacher_id=teacher.id, major_id=major.id)
    db.session.add(class_)
    db.session.commit()
    
    # create student
    student = DB.Student(name="ali", family="alavi", major_id=major.id)
    db.session.add(student)
    db.session.commit()
    
    # query
    print(db.session.query(DB.Major).first().name)
    print(db.session.query(DB.Teacher).first().name)
    print(db.session.query(DB.Class).first().name)
    print(db.session.query(DB.Student).first().name)