"""
MyPy can duck-type objects, regardless of inheritance!
"""
from typing import Sized

# Has no superclass, or metaclass!
class Foobar:
    # But does has a __len__() method that returns ints
    def __len__(self) -> int:
        return 5

def print_length(object: Sized):
    print(len(object))

print_length(Foobar())