"""
details = {
    "Ram":"Lalitpur", 
    "Hari":"Kailali", 
    "Shivani":"Kathmandu", 
}

print(details["Ram"])  # Accesing the element in dictionary

for detail in details:
    print(detail, details[detail], sep = ", ")

"""

"""
How can I store and display contact information for 
multiple people, where each person has a name, address, and job title?

"""
details = {
    "Ram": {"Address": "Lalitpur", "Job": "Doctor"},
    "Hari": {"Address": "Kailali", "Job": "Engineer"},
    "Shivani": {"Address": "Kathmandu", "Job": "Lawyer"},
}

print(details["Ram"]["Job"])  # Accesing the element in dictionary
print(details ["Ram"] ["Address"])
for name, info in details.items():  #details.items() returns ("Ram", {"Address": "Lalitpur", "Job": "Doctor"})
    print(f"{name}: address = {info['Address']}, job = {info['Job']}" )

 

