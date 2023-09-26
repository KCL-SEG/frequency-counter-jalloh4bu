"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        stritem = str(item)
        if stritem in frequencies.keys():
            frequencies[stritem] = frequencies.get(stritem) + 1
        else:
            frequencies[stritem] = 1

    return frequencies
