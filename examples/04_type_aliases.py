"""
Types can be named, for re-use (and readability!)
"""
from typing import Tuple

Coordinate = Tuple[int, int]  # Coordinate is a "type alias"

def move_northwest(x: int, y: int) -> Coordinate:
    return x-1, y+1

def move_east(x: int, y: int) -> Coordinate:
    return x+1, y

assert move_northwest(0, 0) == (-1, 1)
assert move_east(-1, 1) == (0, 1)
