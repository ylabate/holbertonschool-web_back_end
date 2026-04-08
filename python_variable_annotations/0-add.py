#!/usr/bin/env python3
"""Module for adding two floating-point numbers.

This module provides a function that demonstrates basic type annotation
usage in Python, specifically showing how to annotate function parameters
and return types for arithmetic operations.
"""


def add(a: float, b: float) -> float:
    """Add two floating-point numbers and return their sum.

    This function takes two float parameters and returns the result of
    adding them together, demonstrating the use of type annotations for
    function parameters and return values.

    Args:
        a (float): The first floating-point number to add.
        b (float): The second floating-point number to add.

    Returns:
        float: The sum of the two input numbers.
    """
    return a + b
