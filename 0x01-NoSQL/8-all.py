#!/usr/bin/env python3
"""Module: 8-all"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    :param mongo_collection: The MongoDB collection to list documents from.
    :return: A list of all documents, or an empty list if none are found.
    """
    return list(mongo_collection.find())
