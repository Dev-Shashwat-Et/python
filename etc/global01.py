"""
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()

"""
#This above code has an issue with variable scope. The balance variable defined at the top is a global variable, but when you try to modify it inside the functions deposit()
#and withdraw(), Python treats balance as a local variable in those functions, causing the error.

balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

# Use this global keyword sparingly as things can be messy 
