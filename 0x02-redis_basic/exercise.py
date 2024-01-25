#!/usr/bin/env python3
"""Connecting Redis with python"""
import uuid
from typing import Union

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
