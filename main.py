from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # غيّرها لأصول محددة في الإنتاج
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    grade: float

students = [
    Student(id=1, name="Mohammed Emran", grade=5),
    Student(id=2, name="Emran Ali", grade=10),
]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return{'error' : 'Student not found'}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {'message' : 'Student deleted'}
    return {'error' : 'Student not found'}
