"""
# This program implements the concept of self made fucntions inside the class that are called as methods
# By using these methods we're not simply printing some output rather their than we can represent the real world like student abilities in our case in terms function

class Student:
    def __init__(self, name, address, abilities):
        if not name: 
            raise ValueError("Missing name")
        if address not in ["Ktm", "Bhaktapur", "Lalitpur"]:
            raise ValueError("Adress not found")
        self.name = name
        self.address = address
        self.abilities = abilities
    def __str__(self):
        return f"{self.name} is from {self.address}"
    def write(self):
        match self.abilities:
            case "Poem":
                return "❤"
            case "Story":
                return "💕"
            case "Essay":
                return "😍"
            case _:
                return "✔"
            

def main():
    student = get_student()
    print("Epected ability! ")
    print(student.write())
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
def get_student():
    name = input("Name: ")
    address = input("Address: ")
    abilities = input("Abilities: ")
    return Student(name, address, abilities)

if __name__ == "__main__":
    main()
"""
# This program implements the concept of self made fucntions inside the class that are called as methods

class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"{self.name} is from {self.address}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    @property # Getter
    def address(self):
        return self._address
    
    @address.setter # Setter
    def address(self, address):
        if address not in ["Ktm", "Bhaktapur", "Lalitpur"]:
            raise ValueError("Address is not found")
        self._address = address

            
def main():
    student = get_student()
    # student.address = "Sailung" # This is limitations from the class that a programmer can over-ride the class attributes
    print(student)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
def get_student():
    name = input("Name: ")
    address = input("Address: ")
    return Student(name, address)

if __name__ == "__main__":
    main()
