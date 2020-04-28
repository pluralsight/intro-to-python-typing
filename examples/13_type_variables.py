"""
TypeVar allows for consistency (without specifying types)
"""
from typing import Iterable, Optional, TypeVar

T = TypeVar('T')

def get_first_item(things: Iterable[T]) -> Optional[T]:
    for thing in things:
        return thing
    return None

assert get_first_item([1, 2, 3]) == 1
assert get_first_item((1, 2, 3)) == 1
assert get_first_item({'A': 1, 'B': 2, 'C': 3}) == 'A'
