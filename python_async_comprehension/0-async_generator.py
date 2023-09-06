#!/usr/bin/env python3
""" Yields 10 random numbers """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yields 10 random numbers """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
