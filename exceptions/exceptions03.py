
"""
# Concept of reusability
def main():
    age = get_int("What's your age? ")
    year = get_int("What's the year you were born? ")
    print(f"Age is {age} and year of birth is {year}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
"""

# Without passing parameters - less reusable approach
def main():
    age = get_age()
    year = get_birth_year()
    print(f"You are {age} years old, born in {year}")

def get_age():
    while True:
        try:
            return int(input("What's your age? "))           
        except ValueError:
            pass

def get_birth_year():
    while True:
        try:
            return int(input("What year were you born? "))           
        except ValueError:
            pass

main()


