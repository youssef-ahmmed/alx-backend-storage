#!/usr/bin/env python3
"""Connecting Redis with python"""
import uuid
from typing import Union, Callable, Optional

import redis


class Cache:
    """Cache class for connecting to redis"""
    def __init__(self) -> None:
        """Init the redis connection"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
