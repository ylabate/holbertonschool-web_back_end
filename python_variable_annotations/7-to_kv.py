#!/usr/bin/env python3
"""Module for converting key-value pairs into tuples with squared values.

This module provides a function that demonstrates type annotations for
function parameters and return types when working with unions of numeric
types and tuples. The function takes a string key and a numeric value,
then returns a tuple containing the original key and the squared value
converted to a float type. This showcases how to use Union types and
Tuple types in Python type annotations.
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
        A tuple containing the string key and the squared numeric value
        as float.
    """
    return (k, float(v**2))
