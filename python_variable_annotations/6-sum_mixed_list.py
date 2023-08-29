#!/usr/bin/env python3
""" Adds a mixed list """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns the sum of the list """
    res: float = 0
    for value in mxd_list:
        res += value
    return res
