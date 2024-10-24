#!/usr/bin/env python3
"""Module: exercise"""
import redis
from uuid import uuid4
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) \
            -> Union[str, bytes, int, float]:
        """
        Retrieve data from the Redis database.

        :param key: The key under which the data is stored.
        :param fn: An optional conversion function to apply to the data.
        :return: The data stored at the specified key,
                optionally converted using the provided function.
        """
        return self._redis.get(fn(key) if fn else key)

    def get_str(self, key: str) -> str:
        """Retrieve a string from the Redis database."""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Retrieve an integer from the Redis database."""
        return self.get(key, int)
