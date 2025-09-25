"""Lists are one of Python's most versatile 
and commonly used data structures. They are ordered, mutable (changeable), and allow duplicate elements.
"""
#creating list
#creating empty list
empty_list = []
empty_lisT = list()
print (empty_list)
print(empty_lisT)

#creating list with elements
mobile_brands = ["nokia","iphone", "redmi","samsung","nothing"]
numbers = [22,12,2,1,90,0]
mixed = ["nokia",22,"hari",2,1,"iphone"]
print(mobile_brands)

#mutability in list 
print(f"ID of elements before modification{id(numbers)}")
numbers.append(45)  #adds elements at the end
print(f"list after appending is: {numbers}") 
numbers.extend([23,34,53]) #adds list of elements at the end, and extend always takes multiple elements
print(f"list after extending  is: {numbers}") 

print(f"ID of elements after modification {id(numbers)}")

#adding elements in specific position
numbers.insert(4,85) #adds 85 at fifth position
print(f"After insertion: {numbers}")

#adding elements by index
numbers[6] = 1000
print(f"numbers after inserting 1000 at 6th position{numbers}")



#accesing the list
print(mobile_brands[0]) #first element
print (mobile_brands[-1]) #last element



