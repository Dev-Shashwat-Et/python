"""
A float is a fundamental data type designed to represent real numbers. These are numbers that can have a fractional part, meaning they can contain a decimal point.

Examples: 3.14159, -0.005, 2.0, 6.022e23 (scientific notation)

"""


""""
# Using float and round function
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
print(z) """

"""
# Showing output with commas 
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y) # Rounds off the output

print (f"{z:,}")

"""



# Rouding specific position digits
x = float(input("What's x? "))
y = float(input("What's y? "))

#z = round(x/y, 2) # Rounds off the output

#print (f"{z}")

z = (x/y) # Rounds off the output
print(f"{z:.2f}") # another way 



