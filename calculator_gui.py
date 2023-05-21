# Import modules
import tkinter as tk
from calculator import Calculator
from input_validation import InputValidation

# Define class for GUI using tkinter
class TkinterGUI():
    # Initialize init method
    def __init__(self):
        self.calc = Calculator()
        self.iv = InputValidation()
        
        # Sets window and title
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("500x400")
        
        # Create a dropdown menu for math operations
        self.operation_var = tk.StringVar(value="Select Operation")     # A StringVar to store selected operations
        operations = ["Addition", "Subtraction", "Multiplication", "Division"]
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

        # A Calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        # A Clear button 
        self.calculate_button = tk.Button(self.window, text="Clear", command=self.clear)
        self.calculate_button.pack()

        # A result feature
        self.result_label = tk.Label(self.window)
        self.result_label.pack()

    def calculate(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        operation = self.operation_var.get()

        if num1 and num2 and operation != "Select Operation":
            num1 = float(num1)
            num2 = float(num2)

            if operation == 'Addition':
                result = self.calc.add(num1, num2)
            elif operation == 'Subtraction':
                result = self.calc.subtract(num1, num2)
            elif operation == 'Multiplication':
                result = self.calc.multiply(num1, num2)
            elif operation == 'Division':
                result = self.calc.divide(num1, num2)

            
            self.result_label.config(text='Result: {}'.format(result))


    # A method that clears the 
    def clear(self):
        self.operation_var.set("Select Operation") # Reset the operation menu to the initial value
        self.num1_entry.delete(0, tk.END)  # Clear the first number entry
        self.num2_entry.delete(0, tk.END)  # Clear the second number entry
        self.result_label.config(text="")  # Clear the result label

# Instance of Tkinter GUI to run the GUI 
if __name__ == "__main__":
    gui = TkinterGUI()
    gui.window.mainloop()


