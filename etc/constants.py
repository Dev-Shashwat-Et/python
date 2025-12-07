"""
# Simple way to tell other people that you've declared constant 
MEOWS = 3
for _ in range(MEOWS):
    print("meow")
"""


# Using OOP
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()