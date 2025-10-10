
"""
with open("employee.csv") as file:
    for line in file:
       row = line.rstrip().split(",")
       print(f"{row[0]} lives in {row[1]}")
"""
"""
# Sorting the data - this apporach sorts data because of nature of english language accidentally
employees = []
with open("employee.csv") as file:
    for line in file:
       name, address = line.rstrip().split(",")
       employees.append(f"{name} lives in {address}")

for employee in sorted (employees):
    print(employee)
"""

"""
# Sorting data in employee.csv conciously as per either name or address
employees = []
with open("employee.csv") as file:
    for line in file:
       name, address = line.rstrip().split(",")
       employee={}
       employee = {"name": name, "address": address}
       #employee['name'] = name
       #employee['address'] = address
       employees.append(employee)
       
def get_name(employee): # Simlarly, you can define fucntion for address also to sort on the basis of address key
    return employee["name"]
for employee in sorted(employees, key = get_name):
    print(f"{employee['name']} lives in {employee['address']}")
"""

# Sorting data in employee.csv concsiously as per either name or address using lambda function
employees = []
with open("employee.csv") as file:
    for line in file:
       name, address = line.rstrip().split(",")
       employee={}
       employee = {"name": name, "address": address}
       employees.append(employee)
       

for employee in sorted(employees, key = lambda employee: employee["name"]):
    print(f"{employee['name']} lives in {employee['address']}")
