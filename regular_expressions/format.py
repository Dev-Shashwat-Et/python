"""
# If you want to extract different kind of csv, text or any kind of the data that user have submitted in the forms
# Then we can perform this task with help of regular expresions as well
name = input("What's your name? ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")

# This program breaks if the input is like Shashwat,Kadayat to make it more robust we need to use regular 
# Expreession but split function is for string that doesn't RE. For that we've to import Re lib
"""

"""
# This program is extracting the user input incase he enters name in the format Messi, Leonel and then we
# Want to convert it into Leonel Messi
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    #last = matches.group(1)  # Second Way
    #first = matches.group(2)
    #last, first = matches.groups() # One way
    #name = f"{first} {last}"

    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
"""

# Using := (Walrus Operator): that allows assignment and return of value at the same time
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
