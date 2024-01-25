#!/usr/bin/env python3
"""Connecting Redis with python"""
import uuid
from typing import Any

import redis


class Cache:

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
