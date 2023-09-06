#!/usr/bin/env python3
""" Updates topics """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Updates topics """
    query = {"name": name}
    values = {"$set": {"topics": topics}}
    return mongo_collection.update_many(query, values)
