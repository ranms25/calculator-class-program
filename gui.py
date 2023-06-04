# Import modules
import tkinter as tk
from tkinter import ttk
from calculator import Calculator
from user_validation import UserValidation

# Define class for GUI using tkinter
class TkinterGUI():
    # Initialize init method
    def __init__(self):
        self.calc = Calculator()
        self.uv = UserValidation() 

        # Sets window, name, and title
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("500x350")
        self.title_label = ttk.Label(self.window, text="MY CALCULATOR", font=('Arial', 16, 'bold'), foreground='purple')
        self.title_label.pack(pady=15)

        # Create a ttk style and apply the "Adapta" theme
        style = ttk.Style(self.window)
        style.theme_use("vista")
        
        # Create a dropdown menu for math operations
        self.operation_var = tk.StringVar(value="Select Operation")     # A StringVar to store selected operations
        operations = ["Addition", "Subtraction", "Multiplication", "Division"]
        self.operation_menu = tk.OptionMenu(self.window, self.operation_var, *operations)
        self.operation_menu.config(width=15, height=1)
        self.operation_menu.pack(pady=15)

        # An input feature for first number
        self.num1_label = ttk.Label(self.window, text="First number:")
        self.num1_label.pack()
        self.num1_entry = ttk.Entry(self.window)
        self.num1_entry.pack()

        # An input feaure for second number
        self.num2_label = ttk.Label(self.window, text="Second number:")
        self.num2_label.pack()
        self.num2_entry = ttk.Entry(self.window)
        self.num2_entry.pack()    

        # A Calculate button
        self.calculate_button = ttk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack(side=tk.BOTTOM, anchor=tk.N, fill=tk.X)

        # A Clear button
        self.clear_button = ttk.Button(self.window, text="Clear", command=self.clear)
        self.clear_button.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X)

        # A result feature
        self.result_label = ttk.Label(self.window)
        self.result_label.pack()

    # A method that uses imports 
    def calculate(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        operation = self.operation_var.get()   

        try:
            result = self.uv.validate_user(num1, num2, operation)
            if result is not None:
                self.result_label.config(text="\nResult: " + str(result), font=('Verdana', 12, 'bold'))
        except Exception as error:
            self.result_label.config(text=str(error), font=('Helvetica', 10, 'italic'))

    # A method that clears the inputs and selection of the user
    def clear(self):
        self.operation_var.set("Select Operation") # Reset the operation menu to the initial value
        self.num1_entry.delete(0, tk.END)  # Clear the first number entry
        self.num2_entry.delete(0, tk.END)  # Clear the second number entry
        self.result_label.config(text="")  # Clear the result label

# Instance of Tkinter GUI to run the GUI 
if __name__ == "__main__":
    gui = TkinterGUI()
    gui.window.mainloop()