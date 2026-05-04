# import FastAPI
# FastAPI is the "predefined class", used to develop "API calls" GET,POST,PUT,DELETE,....
from fastapi import FastAPI

# import BaseModel
# define Schema
from pydantic import BaseModel

# instantiate FastAPI
app = FastAPI()

# Define Schema
class Employee(BaseModel):
    emp_id:int
    emp_name:str
    department:str
    salary:float
    experience:int
    email:str
    is_active:bool

# connect to db (MongoDB / Oracle / MySQL / VectorDB)
# Dummy DB
employees = [{
    "emp_id":111,
    "emp_name":"Emp1",
    "department":"CSE",
    "salary":10000,
    "experience":2,
    "email":"emp1@gmail.com",
    "is_active":True
},{
    "emp_id":222,
    "emp_name":"Emp2",
    "department":"IT",
    "salary":20000,
    "experience":2,
    "email":"emp2@gmail.com",
    "is_active":True
}]

# GET
@app.get("/")
def home():
    return {"message":"welcome to Employee CRUD Operations !!!"}

# GET
@app.get("/employees")
def get_all_employees():
    return {"total_employees":len(employees),
            "data":employees}

# GET 
@app.get("/employee/{emp_id}")
def get_employee(emp_id:int):
    for emp in employees:
        if emp["emp_id"] == emp_id:
            return emp
    return {"message":"Employee Not Found !!!"}