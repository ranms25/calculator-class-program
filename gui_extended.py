# import necessary module
from gui import TkinterGUI
from calculator_extended import CalculatorExtended
from user_validation import UserValidation


from calculator_extended import CalculatorExtended
# create a class
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