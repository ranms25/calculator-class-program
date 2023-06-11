import pytest
from calculator import Calculator

# Test the addition method
def test_add():
    calculator = Calculator()
    assert calculator.add(2, 3) == 5

# Test the subtraction method
def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 3) == 2

# Test the multiplication method
def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(2, 3) == 6

# Test the division method
def test_divide():
    calculator = Calculator()
    assert calculator.divide(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)
