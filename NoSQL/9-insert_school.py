#!/usr/bin/env python3
""" Inserts a new document """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document """
    op = mongo_collection.insert_one(kwargs)
    return op.inserted_id
