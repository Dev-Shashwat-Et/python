"""
# One approach
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
"""

"""
# Another apporach - better than above
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""

"""
# Sorting file as we read - it is better approach when you have to perfom multiple operation like uppercasing, lowercasing, sorting ect..
names = []
with open("names.txt") as file: # even if "r" is not written by default it is read
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
# for name in sorted(names, reverse= True) # You can sort file in reverse order
    print (f"hello, {name}")
"""

"""
# When there is only need of sorting not other functionality like lowercasing,uppercasing and others
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
"""

