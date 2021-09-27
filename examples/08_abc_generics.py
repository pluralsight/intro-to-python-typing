"""
Generic types are available for all Abstract Base Classes
"""
from typing import Iterable, Tuple

def first_and_last(data: Iterable[str]) -> Tuple['str', 'str']:
    first = ''
    for item in data:
        first = item if not first else first
    return first, item

assert first_and_last(('a', 'b', 'c')) == ('a', 'c')
assert first_and_last(['d', 'e', 'f']) == ('d', 'f')
assert first_and_last(['g', 'h', 'i']) == ('g', 'i')
assert first_and_last({'j': 10, 'k': 11, 'l': 12}) == ('j', 'l')

# Try changing line 8 to: first = None
# (MyPy will STILL catch your mistake!)
