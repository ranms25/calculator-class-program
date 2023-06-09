import pytest
from calculator import Calculator

# Create an instance of the Calculator class for testing
@pytest.fixture
def calculator():
    return Calculator()

# Test the addition method
def test_add(calculator):
    assert calculator.add(2, 3) == 5

# Test the subtraction method
def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2

# Test the multiplication method
def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6

# Test the division method
def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)
