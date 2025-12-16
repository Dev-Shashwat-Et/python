# Implementing above program using sys lib

# What this program does is allow user to give input in command line by typing -n number
import sys

if len(sys.argv) == 1:
    print("meow")

elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")

else: 
    print("Usage: mewos.py")