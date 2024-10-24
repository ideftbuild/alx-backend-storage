#!/usr/bin/env python3
"""Module: exercise"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Decorator that track the number of times a function is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for counting the number of calls."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that store the history of inputs
    and outputs for a function."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that tracks its passed argument and function output
        by storing them to redis."""
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


class Cache:
    """cache class for storing data in a Redis databaser."""

    def __init__(self) -> None:
        """Initialize the Cache instance with a Redis connection
        and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
