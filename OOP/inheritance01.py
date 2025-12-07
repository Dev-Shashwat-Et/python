class Wizard:
    def __init__(self, name):
        if not name: 
            raise ValueError("Name is missing")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Griffyndor")
professor = Professor("Severus", "Defense Aganst the Dark Arts")

print(f"Wizard: {wizard.name}")
print(f"Student {student.name} is from {student.house}")
print(f"Professor {professor.name} teaches subject {professor.subject}")
