#!/usr/bin/env python3
"""Module: 10-update_topics"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.

    :param mongo_collection: The MongoDB collection.
    :param name: The name of the school to update.
    :param topics: A list of strings representing the new topics.
    """
    mongo_collection.update_many(
        {"name": name},  # Filter: Find document(s) by name
        {"$set": {"topics": topics}}  # Update: Set the new topics
    )
