from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    PESEL = Column(Integer)
    phone = Column(Integer)
    address = Column(String(200))

    grades = relationship('StudentGrade', back_populates='student')

    def __repr__(self):
        return f'Student: {self.first_name}, {self.last_name}'


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    budget = Column(Float())
    address = Column(String(200))

    courses = relationship('Course', back_populates='department')

    def __repr__(self):
        return f'Department: {self.name}'


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    enrollment_date = Column(DateTime())
    PESEL = Column(Integer())
    phone = Column(Integer())
    address = Column(String(200))

    def __repr__(self):
        return f'Staff: {self.first_name}, {self.last_name}'


class Administrator(Base):
    __tablename__ = 'administrators'

    stuff_id = Column(Integer(), ForeignKey(Staff.id), primary_key=True)
    department_id = Column(Integer(), ForeignKey(Department.id))
    enrollment_date = Column(DateTime())


class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer(), primary_key=True)
    title = Column(String(100))
    credits = Column(Integer())
    department_id = Column(Integer(), ForeignKey(Department.id))
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    price = Column(Float())

    department = relationship('Department', back_populates='courses')
    students_grades = relationship('StudentGrade', back_populates='courses')

    onsite_courses = relationship('OnsiteCourse', back_populates='courses')
    online_courses = relationship('OnlineCourse', back_populates='courses')

    def __repr__(self):
        return f'Course {self.title}'


class CourseInstructor(Base):
    __tablename__ = 'course_instructors'

    course_id = Column(Integer(), ForeignKey(Course.course_id), primary_key=True)
    stuff_id = Column(Integer(), ForeignKey(Staff.id))
    enrollment_date = Column(DateTime())


class StudentGrade(Base):
    __tablename__ = 'students_grades'

    enrollment_id = Column(Integer(), primary_key=True)
    student_id = Column(Integer(), ForeignKey(Student.id))
    course_id = Column(Integer(), ForeignKey(Course.course_id))
    grade = Column(Integer)

    student = relationship('Student', back_populates='grades')
    courses = relationship('Course', back_populates='students_grades')


class OnlineCourse(Base):
    __tablename__ = 'online_course'

    course_id = Column(Integer, ForeignKey(Course.course_id), primary_key=True)
    url = Column(String(200))

    courses = relationship('Course', back_populates='online_courses')


class OnsiteCourse(Base):
    __tablename__ = 'onsite_course'

    course_id = Column(Integer(), ForeignKey(Course.course_id), primary_key=True)
    address = Column(String(100))
    days = Column(Integer())
    time = Column(DateTime())

    courses = relationship('Course', back_populates='onsite_courses')
