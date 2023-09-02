#!/usr/bin/env python3
""" Measures runtime """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_time() -> float:
    """ Measures runtime """
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
