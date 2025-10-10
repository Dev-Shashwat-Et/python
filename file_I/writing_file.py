# File I\O is used to store our program data even after program is closed in command line

"""
# Approach First
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""
# Approach second - better approach without using close()
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


