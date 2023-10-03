#!/usr/bin/python3
'''Defines a text-indentation'''


def text_indentation(text):
    '''Prints a text with 2 new lines after each : ., ? and :

    Args:
        text: The text to be printed
    Raises:
        TypeError: if text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    eol = 0
    while eol < len(text) and text[eol] == ' ':
        eol += 1

    while eol < len(text):
        print(text[eol], end="")
        if text[eol] == "\n" or text[eol] in ".?:":
            if text[eol] in ".?:":
                print("\n")
            eol += 1
            while eol < len(text) and text[eol] == ' ':
                eol += 1
            continue
        eol += 1
