# Implementing exceptions using function

"""
def main():
    x = get_int()
    print(f"x is {x} ")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not integer")
        #else:
            #break
    #return x
        else:   # Better approach as return breaks out of the loop and returns the funtion value at the same time
            return x

main()

"""

"""
# Elimating the else statement
def main():
    x = get_int()
    print(f"x is {x} ")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
            return x
        except ValueError:
            print("x is not integer")
       

main()

"""

"""
def main():
    x = get_int()
    print(f"x is {x} ")

def get_int():
    while True:
        try:
            return int(input("What is x? "))           
        except ValueError:
            #print("x is not integer")      
            pass  # We can also use the keyword pass
main()

"""

"""
# Standard approach
def main():
    x = get_int("What's is x? ")
    print(f"x is {x} ")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))           
        except ValueError:
            pass  
main()

"""









