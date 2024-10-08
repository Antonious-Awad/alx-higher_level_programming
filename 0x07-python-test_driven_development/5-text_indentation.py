#!/usr/bin/python3
""" text_indentation module """


def text_indentation(text):
    """creates 2 new line for each "?.:" and trims whitespaces 

    Args:
        text (str): string text

    Raises:
        TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    i = 0

    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if (text[i] == '\n' or text[i] in '.?:'):
            if (text[i] in '.?:'):
                print("\n")
            i += 1

            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1
