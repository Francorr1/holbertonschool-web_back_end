#!/usr/bin/env python3
""" Does several delays """
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns several delays """
    delay_list: List[float] = []
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
