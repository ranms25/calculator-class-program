import pytest
from calculator_extended import CalculatorExtended

# Create an instance of the CalculatorExtended class for testing
@pytest.fixture
def calculator_extended():
    return CalculatorExtended()

# Test the exponent method
def test_exponent(calculator_extended):
    assert calculator_extended.exponent(2, 3) == 8

