# pagination

## 0-simple_helper_function.py
Function that calculates the start and end index for a given page and page size, returning a tuple of (start_index, end_index) for pagination purposes.

## 1-simple_pagination.py
Server class that paginates a dataset of popular baby names from a CSV file, implementing a get_page method to retrieve specific pages with default page size of 10.

## 2-hypermedia_pagination.py
Server class that provides hypermedia pagination with a get_hyper method returning pagination metadata including page_size, page number, data, next_page, prev_page, and total_pages.

## 3-hypermedia_del_pagination.py
Server class implementing deletion-resilient hypermedia pagination using an indexed dataset, with a get_hyper_index method that handles scenarios where items may be deleted between requests.