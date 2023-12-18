#!/usr/bin/python3
"""
Minimum Operations's Modules
"""


def minOperations(n):
    """
    This method calculates the fewest
    number of operations needed to result in exactly in <H> characters
    with a given a number <n> in the file
    """

    if n <= 1:
        return 0
    num, div, numOfOperations = n, 2, 0

    while num > 1:
        if num % div == 0:
            num = num / div
            numOfOperations = numOfOperations + div
        else:
            div += 1
    return numOfOperations
