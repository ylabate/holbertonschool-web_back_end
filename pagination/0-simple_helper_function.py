#!/usr/bin/env python3

def index_range(page: int, page_size: int):
    first_id = (page - 1) * page_size
    return (first_id, first_id + page_size)
