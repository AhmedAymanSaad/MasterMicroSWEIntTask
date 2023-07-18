import re

class Validator():
    def __init__(self):
        pass

    def getPlotData(self):
        """
        Get the validated plot data.

        Returns:
            tuple: A tuple containing the minimum x-value, maximum x-value, and the function with ability to handle the ^ power notation.
        """
        return float(self.lastValidXMinInput), float(self.lastValidXMaxInput), self.replacePowerNotation(self.lastValidFunctionInput)
    
    def removeSpaces(self, string: str):
        """
        Remove spaces from the given string.
        This is to make sure all data is consistent, so that the user can input "x^2" or "x ^ 2" and get the same result.

        Args:
            string (str): The input string.

        Returns:
            str: The string with spaces removed.
        """
        return string.replace(" ", "")
    
    def forceLowercase(self, string: str):
        """
        Convert the input string to lowercase.
        This is to make sure all data is consistent, so that the user can input "x^2" or "X^2" and get the same result,
        without having to worry about case sensitivity.

        Args:
            string (str): The input string.

        Returns:
            str: The string in lowercase.
        """
        return string.lower()
    
    def containsX(self, string: str):
        """
        Check if the input string contains the character 'x'.
        This is to handle the cases where the user enters an integer only.

        Args:
            string (str): The input string.

        Returns:
            bool: True if 'x' is present in the string, otherwise False.
        """
        return re.search(r"[x]", string) is not None
    
    def replacePowerNotation(self, string: str):
        """
        Replace '^' with '**' in the input string.
        Since Eval function does not support '^' power notation, this is to handle the cases where the user enters '^' instead of '**'.

        Args:
            string (str): The input string.

        Returns:
            str: The string with '^' replaced by '**'.
        """
        return string.replace("^", "**")
    
    def validateVariablesOperations(self, func: str):
        """
        Validate the function input for allowed characters and variables.

        Args:
            func (str): The input function string.

        Returns:
            bool: True if the input is valid, otherwise raises an Exception.

        Raises:
            Exception: If the function input is empty, contains invalid characters,
                or contains variables other than 'x'.
        """
        func = self.removeSpaces(func)
        if func == "":
            raise Exception("Error: Function input is empty.")
        # Check if there are any variables other than 'x' using regex
        if re.search(r"[a-wyz]", func) is not None:
            raise Exception("Error: Function input contains variables other than x.")
        # Check if there are any other characters other than + - / * ^ and 'x' and digits using regex 
        if re.search(r"[^0-9\+\-\*\/\^x]", func) is not None:
            raise Exception("Error: Function input contains invalid characters.")
        return True
            
    def validateFunctionInput(self, func: str):
        """
        Validate the function input.

        Args:
            func (str): The input function string.

        Returns:
            bool: True if the input is valid, otherwise raises an Exception.

        Raises:
            Exception: If the input function is not valid.
        """
        func = self.removeSpaces(func)
        func = self.forceLowercase(func)
        self.lastValidFunctionInput = func
        self.validateVariablesOperations(func)
        return True
    
    def validateNumberInput(self, number: str):
        """
        Validate the number input.

        Args:
            number (str): The input number string.

        Returns:
            bool: True if the input is a valid number, otherwise raises an Exception.

        Raises:
            Exception: If the number input is empty or invalid.
        """
        # Check if the number is empty or contains invalid characters
        # regex \A and \Z are used to match the entire string
        if not number or not re.match(r'(\A(-?\d+(\.\d*)?))\Z', number):
            raise Exception("Error: Number input is invalid.")
        return True

    def validateXMinInput(self, xMin: str):
        """
        Validate the minimum x-value input.

        Args:
            xMin (str): The input minimum x-value string.

        Returns:
            bool: True if the input is valid, otherwise raises an Exception.

        Raises:
            Exception: If the xMin input is empty or invalid, or if it is greater than xMax.
        """
        xMin = self.removeSpaces(xMin)
        self.validateNumberInput(xMin)
        # Check if xMin is greater than xMax
        if self.lastValidXMaxInput is not None:
            if float(xMin) > float(self.lastValidXMaxInput):
                raise Exception("Error: xMin is greater than xMax.")
        self.lastValidXMinInput = xMin
        return True
    
    def validateXMaxInput(self, xMax: str):
        """
        Validate the maximum x-value input.

        Args:
            xMax (str): The input maximum x-value string.

        Returns:
            bool: True if the input is valid, otherwise raises an Exception.

        Raises:
            Exception: If the xMax input is empty or invalid, or if it is less than xMin.
        """
        xMax = self.removeSpaces(xMax)
        self.validateNumberInput(xMax)
        # Check if xMax is less than xMin
        if self.lastValidXMinInput is not None:
            if float(xMax) < float(self.lastValidXMinInput):
                raise Exception("Error: xMax is less than xMin.")
        self.lastValidXMaxInput = xMax
        return True
