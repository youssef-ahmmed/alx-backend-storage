#!/usr/bin/env python3
"""Connecting Redis with python"""
import uuid
from typing import Union, Callable, Optional
from functools import wraps

import redis


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for the decorator method"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)

        return method(self, args, kwargs)

    return wrapper


class Cache:
    """Cache class for connecting to redis"""

    def __init__(self) -> None:
        """Init the redis connection"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the given data with random key"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """"""
        value = self._redis.get(key)

        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get the value of a key and convert it to string"""
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get the value of a key and convert it to integer"""
        return self.get(key, int)
