from fastapi import FastAPI, Query
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "postgresql://postgres@localhost:5434/students"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = "studentsinfo"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True)
    major = Column(String)

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    major: str

class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    email: str
    major: str

    class Config:
        orm_mode = True

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/students/", response_model=list[StudentOut])
def list_students(page: int, page_size: int):
    db = SessionLocal()
    students = db.query(Student).offset((page - 1) * page_size).limit(page_size).all()
    db.close()
    return students
