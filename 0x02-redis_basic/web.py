#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
from functools import wraps
from typing import Callable

import redis
import requests


def count_cache(method: Callable) -> Callable:
    """Counts how many times a particular URL was accessed"""

    @wraps(method)
    def wrapper(url):
        """Wrapper function for the decorated method."""
        redis_client = redis.Redis()
        redis_client.incr(f"count:{url}")

        result = method(url)
        redis_client.setex(f"result:{url}", 10, result)

        return result

    return wrapper


def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL"""
    return requests.get(url).text
