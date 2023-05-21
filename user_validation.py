# import modules
from calculator import Calculator

# Define class for user interface
class UserValidation():
    
    # A method that validates user interaction with the UI
    def user_validation(self, num1, num2, operation):
        self.calc = Calculator()
        if (num1 !='' and num2 !='') and operation != 'Select Operation':
            try:
                num1 = float(num1)
                num2 = float(num2)

            # A method that performs calculations based on the selected operation
                if operation == 'Addition':
                    return self.calc.add(num1, num2)
                if operation == 'Subtraction':
                    return self.calc.subtract(num1, num2)
                if operation == 'Multiplication':
                    return self.calc.multiply(num1, num2)
                if operation == 'Division':
                    return self.calc.divide(num1, num2)

            # Create exception to handle value error
            except ValueError:
                raise ValueError(f"\nCalculator could not recognized \n '{num1}'  or  '{num2}'")        
        else:
            if num1 =='' or num2 =='':
                raise ValueError('\nIt looks like you did not fill all the required values.')
            else:
                raise ValueError('\nHave you chosen a math operation?')