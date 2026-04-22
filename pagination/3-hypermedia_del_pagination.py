#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.
This module provides a Server class to paginate a database of baby names
even when rows are deleted between requests.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset retrieval.
        Returns the dataset cached in the __dataset attribute,
        excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0.
        Returns a dictionary where keys are original indexes and
        values are the data rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of data starting from a specific index,
        handling cases where items might have been deleted.
        """
        dataset = self.indexed_dataset()
        assert index is not None and 0 <= index < len(self.dataset())

        data = []
        current_index = index
        while len(data) < page_size and current_index < len(self.dataset()):
            item = dataset.get(current_index)
            if item:
                data.append(item)
            current_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current_index
        }
