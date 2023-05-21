# Import modules
import tkinter as tk
from calculator import Calculator
from user_interface import UserInterface

# Define class for GUI using tkinter
class TkinterGUI():
    # Initialize init method
    def __init__(self):
        self.calc = Calculator()
        self.ui = UserInterface()
        
        # Sets window and title
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("500x400")
        
        # Create a dropdown menu for math operations
        self.operation_var = tk.StringVar(value="Select Operation")     # A StringVar to store selected operations
        operations = ["Add", "Subtract", "Multiply", "Divide"]
        self.operation_menu = tk.OptionMenu(self.window, self.operation_var, *operations)
        self.operation_menu.pack()

        # An input feature for first number
        self.num1_label = tk.Label(self.window, text="First number:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(self.window)
        self.num1_entry.pack()

        # An input feaure for second number
        self.num2_label = tk.Label(self.window, text="Second number:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(self.window)
        self.num2_entry.pack()   

    def run(self):
        self.window.mainloop()

# Instance of Tkinter GUI to run the GUI 
if __name__ == "__main__":
    gui = TkinterGUI()
    gui.run()


