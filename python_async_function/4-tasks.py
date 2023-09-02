#!/usr/bin/env python3
""" Returns a list of new tasks """
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_random(n: int, max_delay: int) -> List[float]:
    """ Returns a list of new tasks """
    float_list: List[float] = []
    for i in range(n):
        float_list.append(await task_wait_random(max_delay))
    return sorted(float_list)
