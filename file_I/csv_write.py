"""
# Writing csv file
import csv 

name = input("What's your name? ")
address = input("Where do you live? ")

with open("employee03.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, address]) # Writerow writes a single row to the CSV file

"""


# Writing csv file using Dictwriter associating name and address
import csv 

name = input("What's your name? ")
address = input("Where do you live? ")

with open("employee03.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "address"])
    writer.writerow({"name": name, "address": address})
