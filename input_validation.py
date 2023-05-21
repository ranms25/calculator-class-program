# Define class for user interface
class InputValidation():

    # A method that prompts user to input two numbers
    def input_validation(self):
        try:
            num1 = float(input(num1))
            num2 = float(input(num2))
        # Exception for value and zero division
        except ValueError:
            print('Invalid')
        except ZeroDivisionError:
            print('Invalid')
        else:
            return num1, num2
