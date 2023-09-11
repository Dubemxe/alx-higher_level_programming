#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    first_char = sentence[0]
    length = len(sentence)
    return (len, first_char)
