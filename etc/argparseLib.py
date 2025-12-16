# In sysLib.py program suppose we want user to type any letters and words or say any other convention, other than just -n 
# then program will be complicated. So it is beter to use argparse library

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# Problem with this program is that when user don't provide any number to the command line

# Improved version of this program