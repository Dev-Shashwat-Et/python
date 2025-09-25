""" Conditionals allow you to execute different blocks of 
code based on whether certain conditions are true or false."""

"""
# Simple way of using conditional using if statement

x = int(input("What's value of x? "))
y = int(input("What's value of y? "))

if x < y:
    print("x is smaller than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

"""

"""
# Better way
x = int(input("What's value of x? "))
y = int(input("What's value of y? "))

if x < y:
    print("x is smaller than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

"""

"""
# Third way 
x = int(input("What's value of x? "))
y = int(input("What's value of y? "))

if x < y:
    print("x is smaller than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
"""

"""
# Using or 
x = int(input("What's value of x? "))
y = int(input("What's value of y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""

"""
# Using not equal to makes program even more simpler
x = int(input("What's value of x? "))
y = int(input("What's value of y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

"""
# Using equal also alternative to above program
x = int(input("What's value of x? "))
y = int(input("What's value of y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")





