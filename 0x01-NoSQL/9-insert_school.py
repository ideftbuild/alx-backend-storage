#!/usr/bin/env python3
"""Module: 9-insert_school"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the collection.

    :param mongo_collection: The MongoDB collection.
    :param document: A dictionary representing the document to be inserted.
    :return: The ID of the inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
