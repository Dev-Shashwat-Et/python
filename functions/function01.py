"""
A function in programming is a self-contained block of code designed to perform a specific, well-defined task.
It encapsulates a set of instructions that can be called (or invoked) from other parts of the program, often multiple times.

"""

"""
#when not using parameters
def hello():
    print("Hello ")

name = input("What's your name? ")

hello()
print(name)


"""
"""
# Using parameters 
def hello(to):
    print("Hello ", to)

name = input("What's your name? ")

hello(name)

"""

"""
# Using default parameters 
def hello(to="world"):
    print("Hello ", to)

hello()
name = input("What's your name? ")
hello(name)

"""

#standard way
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello ", to)

main()



"""
#scope problem
def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("Hello ", name)

main()

"""

"""
# Another simple way
def showName(name,age):
    print(f"Person name is: {name} and age is: {age}")

showName("Ramesh", 23) 
"""














