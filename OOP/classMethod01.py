"""
# In this program we've used separate get_student function is not so good from class perspective as everything should be in class
# Representing concept of encapsulation

class Student:
    def __init__(self, name, address):
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

# So we use class method 
"""


class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"{self.name} is from {self.address}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        address = input("Address: ")
        return cls(name, address)
         
def main():
    student = Student.get()
    print(student)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

if __name__ == "__main__":
    main()

