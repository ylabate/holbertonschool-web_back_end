#!/usr/bin/env python3
"""Module for creating multiplier functions with type annotations."""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Create and return a function that multiplies by a value.

    This function takes a multiplier and returns a new function that
    multiplies any input by that multiplier value.

    Args:
        multiplier: A float value to be used as the multiplier.

    Returns:
        A callable function that takes a float and returns the
        product of that float and the multiplier.
    """
    def func(n: float) -> float:
        """Multiply the given number by the multiplier.

        Args:
            n: A float value to be multiplied.

        Returns:
            The product of n and the multiplier.
        """
        return multiplier * n
    return func
