# import modules
from calculator import Calculator
# Define class for user interface
class UserValidation():

    # A method that validates user interaction with the UI
    def user_validation(self, num1, num2, operation):
        self.calc = Calculator()
        if (num1 is not None and num2 is not None) and operation != 'Select Operation':
            num1 = float(num1)
            num2 = float(num2)

        # A method that performs calculations based on the selected operation
            if operation == 'Addition':
                return self.calc.add(num1, num2)
            elif operation == 'Subtraction':
                return self.calc.subtract(num1, num2)
            elif operation == 'Multiplication':
                return self.calc.multiply(num1, num2)
            elif operation == 'Division':
                return self.calc.divide(num1, num2)
            else:
                raise ValueError('Please choose a math operation!')
            
        elif (num1 is None and num2 is None) and operation != 'Select Operation':
            raise ValueError('It looks like you did not enter a value.')
        else:
            raise ValueError('Have you chosen a math operation?')