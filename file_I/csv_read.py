"""
# Using csv as library allows us to take any number of values in files
import csv # Csv handles all of its formatting
employee= []

with open("employee.csv") as file:
    reader = csv.reader(file)
    for name, address in reader:
        employee.append({"name": name, "address": address})

for employee in sorted(employee, key = lambda employee: employee["name"]):
    print(f"{employee['name']} lives in {employee['address']}")
"""

# Anohter approach: in previous approach we assumed first value is name and second one address. 
# But in this approach we've made in the file clear that first one is name and second one is address to make it more robust
import csv 
employees= []

with open("employee02.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append({"name": row["name"], "address": row["address"]})

for employee in sorted(employees, key = lambda employee: employee["name"]):
    print(f"{employee['name']} lives in {employee['address']}")


