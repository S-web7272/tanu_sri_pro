#when no using data classes

class student:
    def __init__(self,name,age,gender,college,cls):
        self.name=name
        self.age=age
        self.gender=gender
        self.college=college
        self.cls=cls
    
from dataclasses import dataclass

@dataclass
class student2:
    name:str
    age:str
    college:str
    cls:str
    section:str
    gender:str

@dataclass
class marks:
    student:student2
    total:int



if __name__ == "_main_":
    s1 = student('shiv',12,'AERT','7th','B','male')
    s2 = student('raavi',12,'SDFDF','7th','A','female')
    s3 = student('rani',16,'FHGH','11th','D','female')

    print(s1.name)
    print(s2.name)
    print(s1.cls)
    print(s2.cls)
    print(s3.name)
    print(s3.cls)
    print(s3)