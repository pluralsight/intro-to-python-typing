"""
The Callable generic can annotate an expected call signature
"""
from typing import Callable

AnnounceFunc = Callable[[int, ], str]

def callback_later(number: int, callback: AnnounceFunc):
    message: str = callback(number)
    print(message)

def deli_counter_announcer(number: int) -> str:
    return f"Now serving Customer number {number}!"

callback_later(13, deli_counter_announcer)
