#!/usr/bin/env python3
""" Returns the list of elements with a specific topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of elements with a specific topic """
    school = mongo_collection.find({"topics": topic})
    return school
