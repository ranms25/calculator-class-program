# import necessary module
from calculator_extended import CalculatorExtended
from gui import TkinterGUI

# create a class
class ExtendedGUI(TkinterGUI):
    def __init__(self):
        super().__init__()

        # Add "Exponentiation" option to the dropdown menu
        self.operation_menu['menu'].exponent_command(label='Exponentiation', command=lambda: self.operation_var.set('Exponentiation'))