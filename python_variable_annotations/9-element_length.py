#!/usr/bin/env python3
"""Module for calculating lengths of sequences in an iterable."""
import typing


def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Return tuples with each sequence and its length.

    This function iterates through a collection of sequence objects
    and creates tuples pairing each sequence with its integer length,
    returning a list of all these tuples.

    Args:
        lst: An iterable containing sequence objects such as lists,
             tuples, or strings.

    Returns:
        A list of tuples where each tuple contains a sequence and
        its corresponding integer length.
    """
    return [(i, len(i)) for i in lst]
