from calculator import square

"""
# One way to test your code - not so good approach as lines of code is more than code to be tested
def main():
    test_square()
def test_square():
    if square(2) != 4:
        print("2 is not squared 4")
    if square(3) != 9:
        print("e is not squared 9")

if __name__ == "__main__":
    main()

"""

"""
# assert is a keyword used for debugging and testing purposes. It checks if acondition is True, and if not, it raises an AssertionError.
# Using assert keyword only - it is not so user friendly
def main():
    test_square()
def test_square():
    assert square(2) == 4
    assert square (3) == 9
    
   
if __name__ == "__main__":
    main()
"""



# By using try and except along with assert program is little bit user friendly yet still lengthy 
def main():
    test_square()
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("3 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("3 squared was not 0")
   

if __name__ == "__main__":
    main()


