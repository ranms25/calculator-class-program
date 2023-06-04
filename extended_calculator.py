# import modules
from calculator import Calculator
from user_validation import UserValidation

# inherit Calculator class to Extended Calculator class
class ExtendedCalculator(Calculator, UserValidation):
    def square(self, num1, num2):
        return round(num1 ** num2, 2)