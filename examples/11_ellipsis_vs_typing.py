"""
Ellipsis symbol can be used as a "wildcard" in some types
"""
from typing import Tuple, Callable

# For callables, ... ignores the args, leaving the return type
IntFunc = Callable[..., int]

# For Tuples, ... matches any length of the given type
SomeStrs = Tuple[str, ...]

def get_int(func: IntFunc) -> int:
    return func()

def make_sentence(strs: SomeStrs):
    return ' '.join(strs)

assert get_int(lambda: 42) == 42
assert make_sentence(('hello', 'world')) == 'hello world'

