#!/usr/bin/python3
"""MyInt Module Implementation"""


class MyInt(int):
    def __eq__(self, value):
        """equal operation

        Args:
            value (int): value

        Returns:
            boolean: result of comparison
        """
        return self.real != value

    def __ne__(self, value):
        """not equal operation

        Args:
            value (int): value

        Returns:
            boolean: result of comparison
        """
        return self.real == value
