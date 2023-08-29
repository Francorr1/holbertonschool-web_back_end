#!/usr/bin/env python3
""" Recretaes the given function """
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Recreates the given function """
    return [(i, len(i)) for i in lst]
