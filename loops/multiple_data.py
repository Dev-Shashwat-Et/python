# Implementing list of dictionary

details = [
    {"Name": "Ramesh", "Address": "Kathmandu", "Profession": "Doctor"},
    {"Name": "Sujan", "Address": "Lalitpur", "Profession": "Lawyer"},
    {"Name": "Shivani", "Address": "Bhaktapur", "Profession": "Engineer"},
    {"Name": "Sima", "Address": "Kailali", "Profession": "None"},

]


for detail in details:
    #print(detail["Name"], detail["Address"], detail["Profession"], sep=", ")
    print(f"{detail['Name']}: Address = {detail['Address']}, Profession = {detail['Profession']}")

