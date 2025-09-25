"""In Python, a string is a sequence of characters enclosed within quotes."""

# Ask user for details
#name = input("What's your name ")

# Remove white space from string
#name = name.strip()

# Capitalize users name
#name = name.capitalize()
#name = name.title()

# You can use all other functions in the same line

name = input("What's your name ").strip().title() # Best practice - you can add as many function as you want

# Split users name into first name and last name
# first, last = name.split()

#print(f"Hello {first}")
# say hello to user
print(f"Hello, {name}")

