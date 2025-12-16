# pip install mypy
# mypy filename - to check code with mypy
# Type hints (also called type annotations) are a way to explicitly indicate what data types your variables, function parameters,
#  and return values should be.

"""
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: " ))
meow(number)
"""
"""
# If you want meow return some values
def meow(n: int) -> None: # This none indicates function returns nothing and helps to catch error after executing this with mypy
    for _ in range(n):
        print("meow")

number: int = int(input("Number: " ))
meows: str = meow(number) # when you run this code it returns none as it expect program to return value but it doesn't
print(meows)
"""
# Fixing above code 
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: " ))
meows: str = meow(number)
print(meows, end="")

