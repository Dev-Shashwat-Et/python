"""In Python, a variable is like a labeled jar where you 
store something (data) to use later. You give it a name (label) 
and put a value (content) inside. """

#Rules
#Use letters, numbers, or _ (underscores).

#Can’t start with a number: 1st_place ❌ → first_place ✅.

#Case-sensitive: Age ≠ age.

#Avoid Python keywords: print = 10 ❌ (breaks print() function). 

name = "Shashwat"
age=23
education="BE computer"

#New way using f-string and is the best way
print(f"my name is {name}. Now I'm {age}. Recently I completed my {education}.")

#Older way using commas and concatenation
print("My name is", name + ".", "Now I'm", str(age) + ".", "Recently I finished my", education + ".")

#We can declare in this way too but comma will create unnecessary spaces
print("My name is", name, ".", "Now I'm", age, ".", "Recently I finished my", education, ".")

city = "Kathmandu"
country = "Nepal"
print(f"I love {city}, {country}")

phone = "Iphone"
price = "1000$"

print(f"{phone} is expensive and costs {price}.")
