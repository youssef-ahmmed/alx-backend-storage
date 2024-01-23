#!/usr/bin/env python3
"""Filter based on topic"""
from typing import List

from pymongo import collection


def schools_by_topic(mongo_collection: collection, topic: str) -> List:
    """function that returns the list of school having a specific topic"""
    return mongo_collection.find({'topics': topic})
