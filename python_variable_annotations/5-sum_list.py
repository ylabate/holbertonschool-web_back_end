#!/usr/bin/env python3
"""Module for summing lists of floats with type annotations."""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Sum all float values in a list and return the total.

    Args:
        input_list: A list containing float values to be summed.

    Returns:
        The sum of all float values in the input list as a float.
    """
    return sum(input_list)
