"""
Unions can allow any member of a set of possible types
"""
from typing import Union

Multiplicable = Union[str, int, float]

def multiply(value: Multiplicable, factor: int) -> Multiplicable:
    result = value * factor
    return result

assert multiply(1, 3) == 3
assert multiply("Foo", 3) == "FooFooFoo"
assert multiply(2.5, 2) == 5.0
# A big improvement over our original example. But we can do better...
