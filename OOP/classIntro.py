#Think of classes as blueprints or templates for creating consistent, reusable, and 
# organized code structures.

"""
# Without class

student1_name = "Ram"
student1_age = 15
student1_grade = "A"

student2_name = "Hari"
student2_age = 18
student2_grade = "B"

def student_info(name, age, grade):
    print(f"{name} {age} {grade}")

student_info(student1_name, student1_age, student1_grade)
student_info(student2_name, student2_age, student2_grade)
"""


# With class

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def student_info(self):
        print(f"{self.name}, {self.age}, {self.grade}")
    
student1 = Student("Ram", 15, "A")
student1.student_info()

student2 = Student("Hari", 18, "B")
student2.student_info()
