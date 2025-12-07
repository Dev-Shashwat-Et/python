# This program demonstrates how a single function is being reused multiple times
def main():
    x = int(input("X: "))
    y = int(input("Y: "))  
    multiply = get_num(x,y)
    square_x = get_num(x,x)
    square_y = get_num(y,y)

    print("Mulitplication is:", multiply)
    print("Square of x is: ", square_x)
    print("Square of y is: ", square_y)

def get_num(x, y):
    return x * y

main()