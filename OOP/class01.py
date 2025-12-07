"""
# Simple function to print student name and address
def main():
    name = get_name()
    address = get_address()
    print(f"{name} is lives in {address}")

def get_name():
    return input("Name: ")

def get_address():
    return input("Address: ")
    
if __name__ == "__main__":
    main()
"""

"""
# Approach to return multiple value at the same time 
def main():
    student = get_student()
    if student[0] == "Ramesh":
        student[1] = "Kathmandu"
    print(f"{student[0]} is lives in {student[1]}")

def get_student():
    name = input("Name: ")
    address = input("Address: ")
    # return name, address # It automatically behaves as tuple as you use comma for multiple values
    # return (name, address) # Using explicitly a tuple 
    # return [name, address] 
    
if __name__ == "__main__":
    main()

# In this code when you give input student as Ramesh and Address as Bhaktapur it will throw error as you are trying to override the tuple values
# One more thing is that both tuple and list uses square bracket when access contents of them
"""

"""
# Using dictionary: Cause it is better approach rather using list specially to handle large data cause in list
# You should remember the index value of each data but in case of dictionary it is not the case

def main():
    student = get_student()
    if student["name"] == "Ramesh":
        student["address"] =  "Kathmandu"
    print(f"{student['name']} is from {student['address']}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
def get_student():

    # student = {}
    # student["name"] = input("Name: ")
    # student["address"] = input("Address: ")
    # return student

    name = input("Name: ")
    address = input("Address: ")
    return {"name": name, "address": address}

if __name__ == "__main__":
    main()


"""

# All programs above are using python built in data types but we can make our own data types using classes
# A class is like a blueprint for creating objects.
# Objects are instances of classes — they have data (attributes) and behavior (methods).

class Student:
    ...
def main():
    student = get_student()
    print(f"{student.name} lives in {student.address}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
def get_student():
    student = Student() # Creating object student
    student.name = input("Name: ")
    student.address = input("Address: ")
    return student

if __name__ == "__main__":
    main()
