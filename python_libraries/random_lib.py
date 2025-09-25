"""
In Python, a library (also commonly called a package or module) is a collection of pre-written code, functions, 
and routines that extend the capabilities of the core Python language.

The random library in Python is a built-in module that provides a suite of functions for generating pseudo-random numbers and
 performing random operations on sequences. 
"""

"""
import random
coin = random.choice(["heads", "tails"])
print(coin)
"""

"""
# Using from keyword allows to use choice function specifically
from random import choice
coin = choice(["heads", "tails"])
print(coin)
"""

"""
randint(a, b) is a function that returns a random integer N such that a <= N <= b.

In simpler terms, it picks a random whole number between two numbers you specify, including both endpoints.

import random
number = random.randint(1,15)
print(number)

"""

import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)




