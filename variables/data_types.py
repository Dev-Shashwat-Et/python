"""In Python, data types define the kind of 
value a variable holds. Here's a breakdown of the main built-in data types:"""

name = "Shashwat" #string
Name = "Rabin"
age = 23 #int
gpa = 3.44 #float
is_voting = True #boolean
is_married = False #boolean
hobbies = ["sports", "Music", "Visiting"] #list, Ordered(mutable) collection
ranks = [1,2,3,4] #list
ratings = (3,2,5,5) #tuple, Ordered (Immutable) collection
complex = 3 + 4j #complex

movie_ratings = set([1,2,2,3,5,5]) #set, is a built-in data type used to store a collection of unique, unordered items.
Co_worker_ratings = frozenset([3,4,4,5,5]) 

"""A frozenset is just like a set, but it’s immutable — meaning once it's created, 
you can’t add, remove, or change its elements."""

friend_info = {"name":"Rabin", "age":23} #Dictionary 
loop_numbers =  range (5) #The range(), function in Python is used to generate a sequence of numbers — it's commonly used in loops.
print(
    f"I'm Mr. {name}. I'm currently {age} old. Got gpa of {gpa} in exam. Am I  voting {is_voting}."
    f"Am I married {is_married}"
    f"I prefer{hobbies}."
    f"I've got friend {friend_info}."
    f"Prefer collegaues ratings {Co_worker_ratings} "
    f"I got following {ranks} in my exam."
    f"Solved complex numerical {complex}.I usually give {ratings} to movies."
    f"While looping a program I used range {loop_numbers} in my program"
)

#mutability and immutability concept
#mutable/immutable - elements can be added or removed and viceversa

#mutability in set
age = set([7,3,0,"old"])
print(f"original set {age}")
age.add(4)
print(f"modified set is {age}")


#immutable: This program will throw error if try to add any element thats why frozenset immutable
"""senior_age = frozenset([23,35,45,65])
print(f"original age is {senior_age}")
senior_age.add(33)
print(f"Modified senior age is {senior_age}")"""


"""Other data types are binary data types"""



