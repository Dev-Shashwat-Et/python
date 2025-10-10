"""
# Simple way to validate an email
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else: 
    print("Invalid")
"""

# Specific way to validate an email with specific domain
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else: 
    print("Invalid")