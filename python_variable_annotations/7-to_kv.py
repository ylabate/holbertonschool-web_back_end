#!/usr/bin/env python3
"""Module for converting key-value pairs to tuples with squared values.

This module provides a function that takes a string key and a numeric value,
returning a tuple containing the key and the squared value as a float.
"""
import typing


def to_kv(
    k: str, v: typing.Union[int, float]
) -> typing.Tuple[str, float]:
    """Convert a key-value pair to a tuple with the value squared.

    This function takes a string key and a numeric value (either an integer
    or a float), and returns a tuple containing the original key and the
    squared value converted to a float type.

    Args:
        k: A string representing the key.
        v: A numeric value (int or float) whose square will be calculated.

    Returns:
        A tuple containing the key and its squared value as a float.
    """
    return (k, float(v**2))
