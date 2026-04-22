#!/usr/bin/env python3
"""Pagination helper utilities."""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Calculate start and end index for a given page and page size.

    Args:
        page: The page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing (start_index, end_index) for the given page.
    """
    first_id = (page - 1) * page_size
    return (first_id, first_id + page_size)
