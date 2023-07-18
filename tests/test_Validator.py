# Import necessary libraries and modules
from Validator import Validator
import pytest

"""
This file contains the unit tests for the Validator class.
"""

# Fixture to initialize the Validator object for testing
@pytest.fixture
def validator():
    validator = Validator()
    validator.lastValidFunctionInput = "x"
    validator.lastValidXMinInput = "-10"
    validator.lastValidXMaxInput = "10"
    return validator

# Test cases for the Validator class
# Test the removeSpaces method
def test_removeSpaces_1(validator):
    assert validator.removeSpaces("1 2 3") == "123"

def test_removeSpaces_2(validator):
    assert validator.removeSpaces("123") == "123"

def test_removeSpaces_3(validator):
    assert validator.removeSpaces(" ") == ""

# Test the forceLowercase method
def test_forceLower_1(validator):
    assert validator.forceLowercase("ABC") == "abc"

def test_forceLower_2(validator):
    assert validator.forceLowercase("abc") == "abc"

def test_forceLower_3(validator):
    assert validator.forceLowercase("") == ""

# Test the containsX method
def test_containsX_1(validator):
    assert validator.containsX("x") == True

def test_containsX_2(validator):
    assert validator.containsX("X") == False

def test_containsX_3(validator):
    assert validator.containsX("abc") == False

def test_containsX_4(validator):
    assert validator.containsX("abcx") == True

# Test the replacePowerNotation method
def test_replacePowerNotation_1(validator):
    assert validator.replacePowerNotation("x^2") == "x**2"

def test_replacePowerNotation_2(validator):
    assert validator.replacePowerNotation("x^2^2") == "x**2**2"

def test_replacePowerNotation_3(validator):
    assert validator.replacePowerNotation("x**2") == "x**2"

# Test the getPlotData method
def test_getPlotData_1(validator):
    assert validator.getPlotData() == (-10.0, 10.0, "x")

def test_getPlotData_2(validator):
    validator.lastValidXMinInput = "-20"
    assert validator.getPlotData() == (-20.0, 10.0, "x")

# Test the validateVariablesOperations method
def test_validateVariablesOperations_1(validator):
    assert validator.validateVariablesOperations("x") == True

def test_validateVariablesOperations_2(validator):
    assert validator.validateVariablesOperations("x^2") == True

def test_validateVariablesOperations_3(validator):
    assert validator.validateVariablesOperations("x^2+1") == True

def test_validateVariablesOperations_4(validator):
    assert validator.validateVariablesOperations("x**2") == True

def test_validateVariablesOperations_5(validator):
    with pytest.raises(Exception):                      # test for throwing an exception correctly
        validator.validateVariablesOperations("")

def test_validateVariablesOperations_6(validator):
    with pytest.raises(Exception):
        validator.validateVariablesOperations("a")

def test_validateVariablesOperations_7(validator):
    with pytest.raises(Exception):
        validator.validateVariablesOperations("(x+1)")

# Test the validateNumberInput method
def test_validateNumberInput_1(validator):
    assert validator.validateNumberInput("1") == True

def test_validateNumberInput_2(validator):
    assert validator.validateNumberInput("1.1") == True

def test_validateNumberInput_3(validator):
    with pytest.raises(Exception):
        validator.validateNumberInput("1.1.1")

def test_validateNumberInput_4(validator):
    assert validator.validateNumberInput("-1") == True

def test_validateNumberInput_5(validator):
    assert validator.validateNumberInput("-1.1") == True

def test_validateNumberInput_6(validator):
    with pytest.raises(Exception):
        validator.validateNumberInput("")

def test_validateNumberInput_7(validator):
    with pytest.raises(Exception):
        validator.validateNumberInput("a")

def test_validateNumberInput_8(validator):
    with pytest.raises(Exception):
        validator.validateNumberInput("-")

# Test the validateXMaxInput method
def test_validateXMaxInput_1(validator):
    assert validator.validateXMaxInput("1") == True

def test_validateXMaxInput_2(validator):
    assert validator.validateXMaxInput("1.1") == True

def test_validateXMaxInput_3(validator):
    with pytest.raises(Exception):
        validator.validateXMaxInput("1.1.1")

def test_validateXMaxInput_4(validator):
    assert validator.validateXMaxInput("-1") == True

def test_validateXMaxInput_5(validator):
    with pytest.raises(Exception):
        validator.validateXMaxInput("-100")

def test_validateXMaxInput_6(validator):
    with pytest.raises(Exception):
        validator.validateXMaxInput("")

# Test the validateXMinInput method
def test_validateXMinInput_1(validator):
    assert validator.validateXMinInput("1") == True

def test_validateXMinInput_2(validator):
    assert validator.validateXMinInput("1.1") == True

def test_validateXMinInput_3(validator):
    with pytest.raises(Exception):
        validator.validateXMinInput("1.1.1")

def test_validateXMinInput_4(validator):
    assert validator.validateXMinInput("-1") == True

def test_validateXMinInput_5(validator):
    with pytest.raises(Exception):
        validator.validateXMinInput("100")
