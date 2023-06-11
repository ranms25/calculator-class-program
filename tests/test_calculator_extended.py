import pytest
from calculator_extended import CalculatorExtended

# Test the exponent method
def test_exponent():
    calculator_extended = CalculatorExtended()
    assert calculator_extended.exponent(2, 3) == 8
