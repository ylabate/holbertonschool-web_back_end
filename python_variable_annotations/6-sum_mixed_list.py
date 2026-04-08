#!/usr/bin/env python3
"""
Module for summing mixed lists containing both integers and floats.

This module provides functionality to calculate the sum of a list
that may contain both integer and floating-point numeric values.
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing mixed integer and float values.

    Args:
        mxd_lst: A list containing both integers and floats.

    Returns:
        The sum of all elements in the list as a float.
    """
    return sum(mxd_lst, 0.0)
