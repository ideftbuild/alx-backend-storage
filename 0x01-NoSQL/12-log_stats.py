#!/usr/bin/env python3
"""Module: 12-log_stats"""


if __name__ == '__main__':
    from pymongo import MongoClient

    # Connect to the database
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Get collection
    nginx_collection = client.logs.nginx

    # print total number of logs
    print(f'{nginx_collection.count_documents({})} logs')

    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(
            f'\tmethod {method}: '
            f'{nginx_collection.count_documents({"method": method})}'
        )

    count = (
        nginx_collection
        .count_documents({"method": "GET", "path": "/status"})
    )
    print(
        f'{count} '
        f'status check'
    )
