#!/usr/bin/env python3
""" Returns a function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function """
    def multiply(multiply: float) -> float:
        return multiplier * multiply
    return multiply
