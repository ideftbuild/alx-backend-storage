#!/usr/bin/env python3
"""Module: web"""
from functools import wraps
from typing import Callable
import redis


redis_ = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """Decorator that track the number of times a function is called."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function for tracking the number of calls."""
        redis_.incr(f'count:{url}')
        cached_content = redis_.get(f'result:{url}')
        if cached_content:
            return cached_content.decode('utf-8')

        html = method(url)
        redis_.setex(f'result:{url}', 10, html)
        return html

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Returns the HTML content of the URL."""
    from requests import get
    return get(url).text
