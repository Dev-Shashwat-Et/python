"""
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(24, 80, 12)
weasely = Vault(34, 29, 10)

galleons = potter.galleons + weasely.galleons
sickles = potter.sickles + weasely.sickles
knuts = potter.knuts + weasely.knuts

total = Vault(galleons, sickles, knuts)
print(total)

# Problem with this code is bad design what if we simply can use potter + weasely using operator overloading

"""

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    

potter = Vault(24, 80, 12)
weasely = Vault(34, 29, 10)


total = potter + weasely
print(total)


