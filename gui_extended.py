# import necessary module
from gui import TkinterGUI
from calculator_extended import CalculatorExtended
from user_validation import UserValidation

# Inherit TkinterGUI to ExtendedGUI 
class ExtendedGUI(TkinterGUI):
    
    # create instantation
    def __init__(self):
        super().__init__()

        # Add "Exponentiation" option to the dropdown menu
        self.operation_menu['menu'].add_command(label='Exponentiation', command=lambda: self.operation_var.set('Exponentiation'))
    
    # A method that obtain user input for num1 and num2
    def calculate(self):
        selected_operation = self.operation_var.get()
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get() 
        
        # Instantiate the UserValidation and CalculatorExtended classes
        self.uv = UserValidation()
        self.ce = CalculatorExtended()

        # Try Block to validate user response when they choose exponentiation
        try:
            self.uv.validate_user(num1, num2, selected_operation)
            
            # If user choose exponentiation, the calculation will execute
            if selected_operation == "Exponentiation":
                result = self.ce.exponent(float(num1), float(num2))
                self.result_label.config(text=f"{num1} raise to {num2} is \n" + str(result), font=('Verdana', 12, 'bold'))

            # If not, it will let the parent class perform the chosen operation and catch exception
            else:
                super().calculate()
        except Exception as error:
            self.result_label.config(text=str(error), font=('Helvetica', 10, 'italic'))