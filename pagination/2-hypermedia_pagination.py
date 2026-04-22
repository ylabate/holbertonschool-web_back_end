#!/usr/bin/env python3
"""Server class for paginating baby names data from a CSV file."""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server with an empty cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading from CSV if necessary."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a specific page of the dataset.

        Args:
            page: The page number (default 1).
            page_size: The number of items per page (default 10).

        Returns:
            List[List]: Rows for the requested page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        try:
            return self.dataset()[slice(*self.index_range(page, page_size))]
        except IndexError:
            return []

    def index_range(self, page: int, page_size: int) -> tuple[int, int]:
        """Calculate the start and end index for a given page.

        Args:
            page: The page number (1-indexed).
            page_size: The number of items per page.

        Returns:
            tuple[int, int]: Tuple of (start_index, end_index).
        """
        first_id = (page - 1) * page_size
        return (first_id, first_id + page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return hypermedia pagination information for a specific page.

        Args:
            page: The page number (default 1).
            page_size: The number of items per page (default 10).

        Returns:
            dict: Dictionary with page_size, page, data, next_page, prev_page, total_pages.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        data = dataset[slice(*self.index_range(page, page_size))] if (
            page < total_pages) else []
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
        }
