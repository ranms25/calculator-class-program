# Import modules
import tkinter as tk
from calculator import Calculator
from user_interface import UserInterface

# Define class for GUI using tkinter
class TkinterGUI():
    # Initialize init method
    def __init__(self):
        self.calc = Calculator()
        
        # Sets window and title
        self.window = tk.Tk()
        self.window.title("Simple Calculator")

        # Create a dropdown menu for math operations
        self.operation_var = tk.StringVar(value="Select Operation")
        operations = ["Add", "Subtract", "Multiply", "Divide"]
        self.operation_menu = tk.OptionMenu(self.window, self.operation_var, *operations)
        self.operation_menu.pack()


    # Start an event loop for GUI
    def run(self):
        self.window.mainloop()

# Instance of Tkinter GUI to run the GUI 
if __name__ == "__main__":
    gui = TkinterGUI()
    gui.run()


