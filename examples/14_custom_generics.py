"""
You can define your own Generics, complete with parameters
"""
from typing import Generic, Iterable, TypeVar

T = TypeVar('T')

class MyClass(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def status(self) -> str:
        return f"{self} status: OK, containing {self.value}"

    def get_contents(self) -> T:
        return self.value

def get_all_statuses(items: Iterable[MyClass[int]]):
    for item in items:
        print(item.status())

get_all_statuses([MyClass(1), MyClass(2)])

value: int = MyClass(5).get_contents()

assert value == 5
