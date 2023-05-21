# Import modules
import tkinter as tk
from calculator import Calculator
from user_interface import UserInterface

# Define class for GUI using tkinter
class TkinterGUI():
    # Initialize init method
    def __init__(self):
        self.calc = Calculator()

        self.window = tk.Tk()
        self.window.title("Simple Calculator")


