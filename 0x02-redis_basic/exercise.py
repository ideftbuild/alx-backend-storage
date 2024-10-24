#!/usr/bin/env python3
"""Module: exercise"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """cache class for storing data in a Redis databaser."""

    def __init__(self) -> None:
        """Initialize the Cache instance with a Redis connection
        and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis database and return the generated key.

        :param data: (str | bytes | int | float): The data to store.
        :return str: The key under which the data is stored.
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
