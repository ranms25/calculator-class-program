# import modules
from calculator import Calculator

# Define class for user interface
class UserInterface():

    # A method that prompts user to input two numbers
    def input_numbers(self):
        try:
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
        # Exception for value and zero division
        except ValueError:
            return None
        except ZeroDivisionError:
            return None
        else:
            return num1, num2