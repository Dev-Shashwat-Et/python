"""
Exceptions are events that occur during program execution that disrupt the normal flow of instructions.
They represent errors or unexpected conditions that need to be handled.

"""
"""
# One way
try:
    x = int(input("What is x? "))
    print(f"x is {x}")

except ValueError:
    print("x is not integer ")

"""

"""
# Another approach
try:
    x = int(input("What is x? "))
    
except ValueError:
    print("x is not integer ")

else:
    print("x is {X}")

"""

# Better approach
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not integer ")
    else:
        break

print(f"x is {x}")










