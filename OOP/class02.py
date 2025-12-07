"""
#__init__() is a special built-in method (also called a constructor) in Python.It runs automatically every time an object of a class is created.
# Self is a reference (a variable) that points to the object currently being created or used.
# It allows that object to store and access its own attributes and methods.

class Student:
    def __init__(self, name, address):

        # This is code is for making program more robust that it can address other issues like user not giving input
        if not name: 
            raise ValueError("Missing name")
        if address not in ["Ktm", "Bhaktapur", "Lalitpur"]:
            raise ValueError("Adress not found")
        self.name = name
        self.address = address

def main():
    student = get_student()
    print(f"{student.name} lives in {student.address}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
def get_student():
    name = input("Name: ")
    address = input("Address: ")
    return Student(name, address)

if __name__ == "__main__":
    main()
"""



# What if you want to directly print student rather than printing student.name and student.address
# For this we use __str__ that helps to print(student) as string. __str__ takes only one argument
class Student:
    def __init__(self, name, address):
        if not name: 
            raise ValueError("Missing name")
        if address not in ["Ktm", "Bhaktapur", "Lalitpur"]:
            raise ValueError("Adress not found")
        self.name = name
        self.address = address
    def __str__(self):
        return f"{self.name} is from {self.address}"

def main():
    student = get_student()
    print(student)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
def get_student():
    name = input("Name: ")
    address = input("Address: ")
    return Student(name, address)

if __name__ == "__main__":
    main()