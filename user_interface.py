# import modules
from calculator import Calculator
import tkinter as tk

# Define class for user interface
class UserInterface:

    # A method that prompts user choose between math operations
    def math_operations(self):
        calc = Calculator()

    # A method that prompts user to input two numbers
    def input_nums(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        # Exception for value and zero division
        except ValueError:
            return None
        except ZeroDivisionError:
            return None
        else:
            return num1, num2