import pytest
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore

from MainWindow import Window

"""
This file contains the end-to-end tests for the main window of the application.
The tests are written using pytest and pytest-qt. The tests are run using the
pytest command in the terminal.
"""

# Fixture to initialize the main window for testing
@pytest.fixture
def window(qtbot):
    window = Window()
    qtbot.addWidget(window)
    return window

# Test 1: Checks the initial state and behavior of the function plotter
def test_window_1(window, qtbot):
    errors = []

    # Check if the main window and UI components are initialized properly
    if window is None:
        errors.append("Window is None")
    if window.ui is None:
        errors.append("UI is None")

    # Check if the initial plot exists and represents the correct function (y = x)
    testPlot = window.plotDisplay.axes.lines[0]
    if testPlot is None:
        errors.append("Plot is None")
    xMin = window.ui.xMinInput.text()
    if xMin != "-5":
        errors.append("xMin is not -5")
    xMax = window.ui.xMaxInput.text()
    if xMax != "5":
        errors.append("xMax is not 5")
    func = window.ui.funcInput.text()
    if func != "x":
        errors.append("func is not x")

    # Generate the expected test plot for comparison
    x = np.linspace(-5, 5, 100)
    y = x
    newPlot = plt.plot(x, y)
    xTested, yTested = testPlot.get_xydata().T
    xNew, yNew = newPlot[0].get_xydata().T
    if not (np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew)):
        errors.append("Plot is not correct")

    # Test updating the function, and check if the plot is updated accordingly
    qtbot.keyClicks(window.ui.xMinInput, "0")   # Add 0 to the xMinInput which makes it 50
    qtbot.keyClicks(window.ui.xMaxInput, "0")   # Add 0 to the xMaxInput which makes it 50
    qtbot.keyClicks(window.ui.funcInput, "**2") # Add **2 to the funcInput which makes it x**2
    testPlot = window.plotDisplay.axes.lines[0]
    xNew, yNew = testPlot.get_xydata().T
    # Test if the plot is updated
    if np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew):
        errors.append("Plot is not updated")

    # Check the status label to ensure it displays the correct message
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Enter a function to plot.":
        errors.append("Status is not correct")

    # Generate another test plot with a different function and compare
    new2Plot = plt.plot(np.linspace(-50, 50, 100), np.linspace(-50, 50, 100)**2)
    xTested, yTested = testPlot.get_xydata().T
    xNew, yNew = new2Plot[0].get_xydata().T
    if not (np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew)):
        errors.append(f"Plot2 is not correct, xmin is {window.ui.xMinInput.text()}, xmax is {window.ui.xMaxInput.text()}, func is {window.ui.funcInput.text()}")

    # Assert that no errors occurred during the test
    assert not errors, "Errors occurred:\n{}".format("\n".join(errors))

# Test 2: Checks various error scenarios and status messages
# Note: \b is the backspace character
def test_window_2(window, qtbot):
    errors = []

    # Check the initial status label message
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Enter a function to plot.":
        errors.append("Status1 is not correct")

    # Test various error scenarios for function input
    qtbot.keyClicks(window.ui.funcInput, "x")
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Error: Unable to evaluate the function.":
        errors.append("Status2 is not correct, status is " + checkStatus)

    qtbot.keyClicks(window.ui.funcInput, "\b\b")
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Error: Function input is empty.":
        errors.append("Status3 is not correct, status is " + checkStatus)

    qtbot.keyClicks(window.ui.funcInput, "x")
    qtbot.keyClicks(window.ui.funcInput, "a")
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Error: Function input contains variables other than x.":
        errors.append("Status4 is not correct, status is " + checkStatus)

    qtbot.keyClicks(window.ui.funcInput, "\b")
    qtbot.keyClicks(window.ui.funcInput, "(")
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Error: Function input contains invalid characters.":
        errors.append("Status5 is not correct, status is " + checkStatus)

    # Test error scenario for xMin input
    qtbot.keyClicks(window.ui.funcInput, "\b")
    qtbot.keyClicks(window.ui.xMinInput, "\b\b")
    qtbot.keyClicks(window.ui.xMinInput, "50")
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Error: xMin is greater than xMax.":
        errors.append("Status6 is not correct, status is " + checkStatus)

    # Test input validations and message after clearing invalid input
    qtbot.keyClicks(window.ui.xMaxInput, "\b")
    qtbot.keyClicks(window.ui.xMaxInput, "100")
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Enter a function to plot.":
        errors.append("Status7 is not correct, status is " + checkStatus)

    qtbot.keyClicks(window.ui.xMinInput, "a")
    checkStatus = window.ui.instructionsLabel.text()
    if checkStatus != "Error: Number input is invalid.":
        errors.append("Status8 is not correct")

    # Assert that no errors occurred during the test
    assert not errors, "Errors occurred:\n{}".format("\n".join(errors))
