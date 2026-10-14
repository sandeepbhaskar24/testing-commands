from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# Database connection
engine = create_engine(
    "sqlite:///students.db",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Database table
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


# Create table
Base.metadata.create_all(bind=engine)


# CREATE
@app.post("/students")
def create_student(name: str, age: int):
    db = SessionLocal()

    student = Student(name=name, age=age)
    db.add(student)
    db.commit()
    db.refresh(student)

    result = {
        "id": student.id,
        "name": student.name,
        "age": student.age
    }

    db.close()
    return result


# READ ALL
@app.get("/students")
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()

    result = [
        {"id": s.id, "name": s.name, "age": s.age}
        for s in students
    ]

    db.close()
    return result


# READ ONE
@app.get("/students/{student_id}")
def get_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        db.close()
        return {"message": "Student not found"}

    result = {
        "id": student.id,
        "name": student.name,
        "age": student.age
    }

    db.close()
    return result


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int):
    db = SessionLocal()
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        db.close()
        return {"message": "Student not found"}

    student.name = name
    student.age = age

    db.commit()
    db.refresh(student)

    result = {
        "id": student.id,
        "name": student.name,
        "age": student.age
    }

    db.close()
    return result


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        db.close()
        return {"message": "Student not found"}

    db.delete(student)
    db.commit()
    db.close()

    return {"message": "Student deleted successfully"}