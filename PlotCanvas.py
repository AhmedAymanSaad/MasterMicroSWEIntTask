import sys
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class PlotCanvas(FigureCanvasQTAgg):
    """
    Custom matplotlib figure canvas to display function plots in a PyQt application.
    """

    def __init__(self, parent: QMainWindow, width: int = 5, height: int = 4, dpi: int = 100):
        """
        Initialize the PlotCanvas.

        Args:
            parent (QMainWindow): The parent window to which the canvas will be added.
            width (int, optional): The width of the figure in inches. Defaults to 5.
            height (int, optional): The height of the figure in inches. Defaults to 4.
            dpi (int, optional): The dots per inch resolution of the figure. Defaults to 100.
        """
        self.parent = parent
        fig: Figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(PlotCanvas, self).__init__(fig)
        toolbar: NavigationToolbar = NavigationToolbar(self, parent)

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget: QWidget = QWidget()
        widget.setLayout(layout)
        
        layoutPlot: QVBoxLayout = parent.ui.plotWidget
        layoutPlot.addWidget(widget)

    def plot(self):
        """
        Plot the function based on the validated input provided by the parent window's validator.

        Raises:
            Exception: If there is an error while evaluating the function or if the function contains invalid characters.
        """
        # Clear the axes and get the validated plot data from the parent window's validator
        self.axes.clear()
        xMin: float = None
        xMax: float = None
        func: str = None
        xMin, xMax, func = self.parent.validator.getPlotData()
        x = np.linspace(xMin, xMax, 100)
        try:
            if self.parent.validator.containsX(func):
                # Create a lambda function for the input expression
                f = lambda x: eval(func)
                # Evaluate the function for each x value
                y = f(x)
                self.axes.plot(x, y)
            else:
                # If the function does not contain 'x', treat it as a constant function
                f = eval(func)
                self.axes.axhline(y=f, color='r', linestyle='-')

            self.axes.set_xlabel('x')
            self.axes.set_ylabel('f(x)')
            self.axes.set_title(f'Plot of {func}')
            self.axes.grid(True)
            self.draw()

        except:
            raise Exception("Error: Unable to evaluate the function.")
