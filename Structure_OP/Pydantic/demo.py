from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'ankit'
    age: Optional[int] = None
    email: EmailStr
    cgpa : float=Field(gt=4.0,lt=10.0,default=6.0,description="A decimal value for cgpa")

new_student= {'age':'22','email':'abc@yahoo.com','cgpa':8.9}

student=Student(**new_student)

print(student.model_dump())
print(student.model_dump_json())