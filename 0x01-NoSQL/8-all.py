#!/usr/bin/env python3
"""List all documents in Python"""
from pymongo import collation


def list_all(mongo_collection: collation):
    """unction that lists all documents in a collection"""
    return mongo_collection.find()
