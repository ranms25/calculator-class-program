# Define class for user interface
from calculator import Calculator
class UserInterface:

    # A method that prompts user to input two numbers
    def input_nums(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2