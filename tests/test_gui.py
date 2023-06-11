import pytest
from gui import TkinterGUI

@pytest.fixture
def gui():
    return TkinterGUI()

def test_calculate(gui):
    # Set the inputs
    gui.num1_entry.insert(0, "2")
    gui.num2_entry.insert(0, "3")
    gui.operation_var.set("Addition")

    # Call the calculate method
    gui.calculate()

    # Check the result
    assert gui.result_label["text"] == "\nResult: 5.0"

def test_clear(gui):
    # Set the inputs
    gui.num1_entry.insert(0, "2")
    gui.num2_entry.insert(0, "3")
    gui.operation_var.set("Addition")

    # Call the clear method
    gui.clear()

    # Check if inputs and selection are cleared
    assert gui.operation_var.get() == "Select Operation"
    assert gui.num1_entry.get() == ""
    assert gui.num2_entry.get() == ""
