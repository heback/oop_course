import os
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, Relationship

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = 'course_management.db'
engine = create_engine(f"sqlite:///{BASE_DIR}/{DB_NAME}", echo=True)

session = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )
)

Model = declarative_base()
Model.query = session.query_property()


class TimeStampedModel(Model):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())


class Category(TimeStampedModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(80), nullable = False)

    subjects = Relationship('Subject', back_populates = 'categories')


    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}"


class Subject(TimeStampedModel):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key = True, autoincrement = True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    name = Column(String(80), nullable = False)

    categories = Relationship('Category', back_populates = 'subjects')


class Course(TimeStampedModel):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key = True, autoincrement = True)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    school_year = Column(String(4), nullable = False)
    semester = Column(String(2), nullable = False)

    subjects = Relationship('Subject', back_populates = 'courses')
    tests = Relationship('Test', back_populates = 'courses')
    course_enrolls = Relationship('CourseEnroll', back_populates = 'courses')


class Test(TimeStampedModel):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key = True, autoincrement = True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    test_type = Column(String(20), nullable = False)
    test_score = Column(Float, nullable = False)

    courses = Relationship('Course', back_populates = 'tests')
    test_enrolls = Relationship('TestEnroll', back_populates = 'tests')


class Student(TimeStampedModel):
    __tablename__ = 'students'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(20), nullable = False)
    grade = Column(String(10), nullable = False)
    classno = Column(String(3), nullable = False)

    course_enrolls = Relationship('CourseEnroll', back_populates = 'students')


class CourseEnroll(TimeStampedModel):
    __tablename__ = 'course_erolls'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key = True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key = True)

    students = Relationship('Student', back_populates = 'course_enrolls')
    courses = Relationship('Course', back_populates = 'course_enrolls')


class TestEnroll(TimeStampedModel):
    __tablename__ = 'test_enrolls'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key = True)
    test_id = Column(Integer, ForeignKey('tests.id'), primary_key = True)
    score = Column(Float, nullable = False)

    students = Relationship('Student', back_populates = 'test_enrolls')
    tests = Relationship('Test', back_populates = 'test_enrolls')
