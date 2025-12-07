"""
import random

class Hat:
    def __init__(self) :
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))   

hat = Hat()
hat.sort("Harry")
"""


"""
If the houses list is shared across all instances (i.e., the same for every hat), you 
could use a class method to emphasize that the sorting logic doesn't depend on instance-specific data:
Also Current - requires instantiation
hat = Hat()  # Why create an object?
hat.sort("Harry")

# Better - direct class usage
Hat.sort("Harry")   More logical - the Hat is singular in Harry Potter
"""

# So better approach is to use @classmethod
import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))   

Hat.sort("Harry")
