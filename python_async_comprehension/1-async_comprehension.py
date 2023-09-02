#!/usr/bin/env python3
""" Returns the result from task 0 """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Returns the result from task 0 """
    res: List[float] = [i async for i in async_generator()]
    return res
