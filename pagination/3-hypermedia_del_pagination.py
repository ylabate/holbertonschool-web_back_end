#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        indexed_dataset = self.indexed_dataset()

        assert isinstance(index, int) and isinstance(page_size, int)
        assert 0 <= index < len(indexed_dataset)

        page = []
        current_index = index
        while len(page) < page_size:
            if indexed_dataset.get(current_index):
                page.append(indexed_dataset[current_index])
            current_index += 1
        return {
            "index": index,
            "data": page,
            "page_size": len(page),
            "next_index": current_index
        }
