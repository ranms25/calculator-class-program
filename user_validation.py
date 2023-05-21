# import modules
from calculator import Calculator
# Define class for user interface
class UserValidation():

    # A method that validates user interaction with the UI
    def user_validation(self, num1, num2, operation):
        if (num1 and num2) and operation != 'Select Operation':
            num1 = float(num1)
            num2 = float(num2)

        # A method that performs calculations based on the selected operation and the provided input numbers
            if operation == 'Addition':
                return Calculator().add(num1, num2)
            elif operation == 'Subtraction':
                return Calculator().subtract(num1, num2)
            elif operation == 'Multiplication':
                return Calculator().multiply(num1, num2)
            elif operation == 'Division':
                return Calculator().divide(num1, num2)
            else:
                raise ValueError('Please choose a math operation.')
        else:
            raise ValueError('It looks like you put an invalid value?')
