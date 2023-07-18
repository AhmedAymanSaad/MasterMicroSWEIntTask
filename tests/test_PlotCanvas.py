import pytest
from MainWindow import Window
import numpy as np
import matplotlib.pyplot as plt

"""
This file contains test for the canvas and the plotting funcitonality of the application.
In order to compare the plots generated by the application, the plot data is set and
then the plot funciton is called to generate the plot in the window, then a dummy plot
of the expected result is generated and the plot data is compared.
"""

@pytest.fixture
def window(qtbot):
    window = Window()
    qtbot.addWidget(window)
    return window

def test_plot_1(window):
    assert window is not None

def test_plot_2(window):
    assert window.ui is not None

def test_plot_3(window):
    axesTested = window.plotDisplay.axes.lines[0]
    # plot x from -5 to 5
    x = np.linspace(-5, 5, 100)
    # plot y = x
    y = x
    # plot on new axes the expected result to compare
    axesNew = plt.plot(x, y)
    # compare the two axes
    xTested, yTested = axesTested.get_xydata().T # extract the data from the displayed plot
    xNew, yNew = axesNew[0].get_xydata().T # extract the data from the expected plot
    assert np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew)

def test_plot_4(window):
    axesTested = window.plotDisplay.axes.lines[0]
    # plot x from -5 to 5
    x = np.linspace(-5, 5, 100)
    # plot y = x
    y = 2*x
    # plot on new axes to compare
    axesNew = plt.plot(x, y)
    # compare the two axes
    xTested, yTested = axesTested.get_xydata().T
    xNew, yNew = axesNew[0].get_xydata().T
    assert not(np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew))

def test_plot_5(window):
    window.ui.xMaxInput.setText("5")
    window.ui.xMinInput.setText("-5")
    window.ui.funcInput.setText("5")
    window.plotDisplay.plot()
    axesTested = window.plotDisplay.axes.lines[0]
    axesNew = plt.axhline(y=5, color='r', linestyle='-')
    # # compare the two axes
    testedData = axesTested.get_data()
    NewData = axesNew.get_data()
    assert np.array_equal(testedData, NewData)

def test_plot_6(window):
    window.ui.xMaxInput.setText("5")
    window.ui.xMinInput.setText("-5")
    window.ui.funcInput.setText("5+5")
    window.plotDisplay.plot()
    axesTested = window.plotDisplay.axes.lines[0]
    axesNew = plt.axhline(y=5, color='r', linestyle='-')
    # # compare the two axes
    testedData = axesTested.get_data()
    NewData = axesNew.get_data()
    assert not(np.array_equal(testedData, NewData))

def test_plot_7(window):
    window.ui.xMaxInput.setText("5")
    window.ui.xMinInput.setText("-5")
    window.ui.funcInput.setText("5+5")
    window.plotDisplay.plot()
    axesTested = window.plotDisplay.axes.lines[0]
    axesNew = plt.axhline(y=10, color='r', linestyle='-')
    # # compare the two axes
    testedData = axesTested.get_data()
    NewData = axesNew.get_data()
    assert (np.array_equal(testedData, NewData))

def test_plot_8(window):
    window.ui.xMaxInput.setText("5")
    window.ui.xMinInput.setText("-5")
    window.ui.funcInput.setText("2*x+x**2")
    window.plotDisplay.plot()
    axesTested = window.plotDisplay.axes.lines[0]
    axesNew = plt.plot(np.linspace(-5, 5, 100), 2*np.linspace(-5, 5, 100)+np.linspace(-5, 5, 100)**2)
    # compare the two axes
    xTested, yTested = axesTested.get_xydata().T
    xNew, yNew = axesNew[0].get_xydata().T
    assert (np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew))

def test_plot_9(window):
    window.ui.xMaxInput.setText("10")
    window.ui.xMinInput.setText("-10")
    window.ui.funcInput.setText("2*x+x**2")
    window.plotDisplay.plot()
    axesTested = window.plotDisplay.axes.lines[0]
    axesNew = plt.plot(np.linspace(-5, 5, 100), 2*np.linspace(-5, 5, 100)+np.linspace(-5, 5, 100)**2)
    # compare the two axes
    xTested, yTested = axesTested.get_xydata().T
    xNew, yNew = axesNew[0].get_xydata().T
    assert not(np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew))

def test_plot_10(window):
    window.ui.xMaxInput.setText("50")
    window.ui.xMinInput.setText("-50")
    window.ui.funcInput.setText("x**2")
    window.plotDisplay.plot()
    axesTested = window.plotDisplay.axes.lines[0]
    axesNew = plt.plot(np.linspace(-50, 50, 100), np.linspace(-50, 50, 100)**2)
    # compare the two axes
    xTested, yTested = axesTested.get_xydata().T
    xNew, yNew = axesNew[0].get_xydata().T
    assert (np.array_equal(xTested, xNew) and np.array_equal(yTested, yNew))