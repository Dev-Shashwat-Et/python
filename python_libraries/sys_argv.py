import sys

"""
The sys module is one of Python's most fundamental built-in modules. Its name is short for "system," and that's exactly what it is: it provides access to variables and functions that interact strongly with the Python interpreter 
and the underlying operating system environment it is running on.

Use:  Automation and Scripting
This is the biggest use. You write a script once and run it with different 
inputs to perform repetitive tasks automatically.
"""

"""
# Handling index error of sys.argv in
try:
    print("My name is ", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
"""
# Another way of handling error
if len(sys.argv) < 2:
    print("Too few arguments")

elif len(sys.argv) > 2:
    print("Too many arguments")

else:
    print("Hello, My name is", sys.argv[1])
"""


"""
# In this program it shows the error if we execute without passing any parameters
if len(sys.argv) < 2:
    ("Too few arguments")

elif len(sys.argv) > 2:
    print("Too many arguments")

print("Hello, my name is", sys.argv[1])
"""

"""
# Above error can be handled using exit function
if len(sys.argv) < 2:
    exit("Too few arguments")

elif len(sys.argv) > 2:
    exit ("Too many arguments")

print("Hello, my name is", sys.argv[1])
"""


# passing multliple arguments:
if len(sys.argv) < 2:
    exit("Too few arguments")

#for arg in sys.argv[1:]: # Slicing from the from the first element of list
for arg in sys.argv[1:-1]: # Slicing from the end as well
    print("Hello, my name is", arg)



