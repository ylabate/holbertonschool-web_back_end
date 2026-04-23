#!/usr/bin/env python3
"""Module that inserts a new document into a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection

    Args:
        mongo_collection: The pymongo collection object
        **kwargs: Arbitrary keyword arguments to be inserted as the document

    Returns:
        The _id of the inserted document
    """
    return (mongo_collection.insert_one(kwargs).inserted_id)
