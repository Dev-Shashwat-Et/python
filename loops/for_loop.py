"""
The for loop in Python is used to iterate over items in any iterable 
object (like a list, tuple, string, etc.).
"""
"""
# Simple way but not good for larger number
for i in [0,1,2]:
    print("Hello")
"""

"""
# Using range
#for i in range(3):
for _ in range(5):  # i also can be replaced by underscore
    print("Hello")
"""
"""
# Advanced type not so standard - Not recommended
print("Hello\n" * 3, end="")
"""

# Executing loop only until input as positive numbers  from the user using loop

while True:
    n = int(input("What's n? "))
    # if n < 0:
    #     continue
    # else:
    #     break

    if n > 0:
        break
for _ in range(n):
    print("Hello")



