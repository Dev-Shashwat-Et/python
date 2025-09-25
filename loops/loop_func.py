
"""
# Loop using function, only executing program for positive numbers
def main():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    hello(n)

def hello(n):  
    for _ in range(n):
        print("Hello")

main()
"""
# Better approach
def main():
        number = get_number()
        hello(number)

def get_number():
    while True:
       n = int(input("What's n? "))
       if n > 0:
            return n
    #        break  # You can also use break here but you'll again have to use return
    # return n 
         
def hello(n):
    for _ in range(n):
        print("Hello")

main()