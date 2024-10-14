#!/usr/bin/python3
"""MyInt Module Implementation"""


class MyInt(int):
    def __init__(self):
        super().__init__()

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
