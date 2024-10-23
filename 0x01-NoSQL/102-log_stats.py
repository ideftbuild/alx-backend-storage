#!/usr/bin/env python3
"""Module: 12-log_stats"""


if __name__ == '__main__':
    from pymongo import MongoClient, DESCENDING

    # Connect to the database
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Get collection
    nginx = client.logs.nginx

    # print total number of logs
    print(f'{nginx.count_documents({})} logs')

    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(
            f'\tmethod {method}: {nginx.count_documents({"method": method})}'
        )
    count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f'{count} status check')
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        }, {
            "$sort": {
                "count": -1,
            }
        },
        {
            "$limit": 10
        }
    ]

    print('IPs:')
    for stat in nginx.aggregate(pipeline):
        print(f'\t{stat.get("_id")}: {stat.get("count")}')
