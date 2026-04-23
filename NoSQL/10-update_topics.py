#!/usr/bin/env python3
"""Module that updates topics for a document in a MongoDB collection"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a document by name

    Args:
        mongo_collection: The pymongo collection object
        name: The name of the document to update
        topics: A list of topics to set for the document

    Returns:
        None
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
