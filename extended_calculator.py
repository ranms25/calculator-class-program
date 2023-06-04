# import modules
from calculator import Calculator
from user_validation import UserValidation

# inherit Calculator class to Extended Calculator class
class ExtendedCalculator(Calculator, UserValidation):
    # a NEW method for exponentiation
    def square(self, num1, num2):
        return round(num1 ** num2, 2)

    # a validation methof for exponentiation
    def calculate(self, num1, num2, operation):
        self.validate_user()  # Implement user validation first before calculation by calling validate_user method in UserValidation class