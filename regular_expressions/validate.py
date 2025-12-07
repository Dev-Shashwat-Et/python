"""
# Simple way to validate an email
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else: 
    print("Invalid")
"""

"""
# Specific way to validate an email with specific domain, but this program not good as well like if we add
# name@.edu yet it treats that as correct
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else: 
    print("Invalid")


# As this program displays input of name@.edu as valid so in order to make it to check if there is something
# prior to . we may need to use another split function which is not good approach 

"""
# Good approach using re library that addresses all the stuffs to be checked
import re

email = input("What's your email? ")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): #\w = [a-zA-z_]
    print("Valid")
else:
    print("Invalid")