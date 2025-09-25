
"""
# Standard method for writing testing code using pytest - which handles all exceptions
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# But the problem with this test is only showing one line is buggy and showing regarding other lines

"""
import pytest # For type-error
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")



