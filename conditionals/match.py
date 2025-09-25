"""In Python, the match statement (introduced in Python 3.10) 
provides structural pattern matching functionality. """

"""
# Way to check multiple conditions
brand = input("What's your brand? ")

if brand == "iphone":
    print("Premium")
elif brand == "samsung":
    print("Premium")
elif brand == "gucci":
    print("Premium")
else: 
    print("Not found")
"""

"""
# Another Way to check multiple conditions
brand = input("What's your brand? ")

if brand == "iphone" or brand == "samsung" or brand == "gucci":
    print("Premium")
else: 
    print("Not found")
"""

"""
# Using match
brand = input("What's your brand? ")

match brand:
    case "iphone":
        print("Premium")
    case "samsung":
        print("Premium")
    case "gucci":
        print("Premium")
    case _:
        print("Not found")
"""

# Another way using match
brand = input("What's your brand? ")

match brand:
    case "iphone" | "samsung" | "Gucci":
        print("Premium")
    case "xioami":
        print("Budget")
    case _:
        print("Not found")



