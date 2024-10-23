#!/usr/bin/env python3
"""Module: 101-students"""
from pymongo import MongoClient, DESCENDING


def top_students(mongo_collection):
    """
    Retrieve all documents from the specified MongoDB collection and
    sort them by the average score attribute in descending order.

    :param mongo_collection: The pymongo collection object to query.

    :return: A cursor that contains the sorted documents.
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"  # Calculate the average score
                }
            }
        },
        {
            "$sort": {
                "averageScore": DESCENDING
            }
        }
    ]

    return mongo_collection.aggregate(pipeline)
