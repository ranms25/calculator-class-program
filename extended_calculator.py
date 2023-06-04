# import modules
from calculator import Calculator
from user_validation import UserValidation

# inherit Calculator class to Extended Calculator class
class ExtendedCalculator(Calculator, UserValidation):
    # A NEW method for exponentiation
    def square(self, num1, num2):
        return round(num1 ** num2, 2)

    # A validation method for exponentiation
    def calculate(self, num1, num2, operation):
        self.validate_user()  # Implement user validation first before calculation by calling validate_user method in UserValidation class

        # A method that will perform calculation if the user choose this operation
        if operation == 'Exponentiation':
            return self.square(num1, num2)