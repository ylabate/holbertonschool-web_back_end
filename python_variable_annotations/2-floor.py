#!/usr/bin/env python3
"""Module that provides a function to convert a float to its rounded
integer value with type annotations.
"""


def floor(n: float) -> int:
    """Returns the floor value of a float as an integer using rounding.

    Args:
        n: A float number to be rounded.

    Returns:
        The rounded integer value of the input float.
    """
    return round(n)
