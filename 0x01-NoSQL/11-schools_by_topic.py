#!/usr/bin/env python3
"""Module: 11-schools_by_topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.

    :param mongo_collection: The MongoDB collection.
    :param topic: The topic to search for.
    :return: A list of school documents that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
