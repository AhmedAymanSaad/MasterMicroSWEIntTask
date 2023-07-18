from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtCore import Slot
from PySide2.QtUiTools import QUiLoader
from UIMainWindow import Ui_MainWindow  # UI layout class
from PlotCanvas import PlotCanvas      # Custom plot canvas class
from Validator import Validator        # Input validation class

class Window(QMainWindow):
    def __init__(self, parent: QMainWindow = None):
        super(Window, self).__init__(parent)
        # Load the UI layout using the UiLoader and set it up
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set the initial instruction text
        self.ui.instructionsLabel.setText("Enter a function to plot.")

        # Initialize the Validator to handle input validation
        self.validator: Validator = Validator()
        self.validator.lastValidFunctionInput: str = self.ui.funcInput.displayText()
        self.validator.lastValidXMinInput: str = self.ui.xMinInput.displayText()
        self.validator.lastValidXMaxInput: str = self.ui.xMaxInput.displayText()

        # Initialize the PlotCanvas to handle plotting
        self.plotDisplay: PlotCanvas = PlotCanvas(self, width=5, height=4, dpi=100)
        self.plotDisplay.plot()

        # Connect the input fields to their corresponding handlers
        self.ui.funcInput.textChanged.connect(self.handleFunctionInputChange)
        self.ui.xMinInput.textChanged.connect(self.handleXMinInputChange)
        self.ui.xMaxInput.textChanged.connect(self.handleXMaxInputChange)

    @Slot()
    def handleFunctionInputChange(self):
        # Slot for handling changes in the function input field
        try:
            self.validator.validateFunctionInput(self.ui.funcInput.displayText())
            self.plotDisplay.plot()  # Plot the function using the updated input
            self.ui.instructionsLabel.setText("Enter a function to plot.")
        except Exception as e:
            # If an error occurs during validation, display the error message
            self.ui.funcInput.setText(self.validator.lastValidFunctionInput)
            print(e)
            self.ui.instructionsLabel.setText(str(e))

    @Slot()
    def handleXMinInputChange(self):
        # Slot for handling changes in the xMin input field
        try:
            self.validator.validateXMinInput(self.ui.xMinInput.displayText())
            self.plotDisplay.plot()  # Plot the function using the updated input
            self.ui.instructionsLabel.setText("Enter a function to plot.")
        except Exception as e:
            # If an error occurs during validation, display the error message
            print(e)
            self.ui.instructionsLabel.setText(str(e))

    @Slot()
    def handleXMaxInputChange(self):
        # Slot for handling changes in the xMax input field
        try:
            self.validator.validateXMaxInput(self.ui.xMaxInput.displayText())
            self.plotDisplay.plot()  # Plot the function using the updated input
            self.ui.instructionsLabel.setText("Enter a function to plot.")
        except Exception as e:
            # If an error occurs during validation, display the error message
            print(e)
            self.ui.instructionsLabel.setText(str(e))

if __name__ == "__main__":
    # Application entry point
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
