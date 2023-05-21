# import modules
import tkinter as tk
from calculator import Calculator

# Define class for user interface
class TkinterGUI():

    # A constructor that initializes instance of calculator class
    def __init__(self):
        self.calc = Calculator()

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