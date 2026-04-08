#!/usr/bin/env python3
"""Module that implements a type-annotated floor function for float values.

This module provides a function that takes a floating-point number as input
and returns the floor of that number as an integer, demonstrating proper
type annotation usage in Python for mathematical operations.
"""
import math


def floor(n: float) -> int:
    """Returns the floor of a float value as an integer.

    Args:
        n: A float number to get the floor value of.

    Returns:
        The floor of the input float as an integer value.
    """
    return math.floor(n)
