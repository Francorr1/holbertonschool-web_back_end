#!/usr/bin/env python3
""" Adds a list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of the list """
    res: float = 0
    for value in input_list:
        res += value
    return res
