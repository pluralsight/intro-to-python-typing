"""
Protocols allow for inheritance-free static structural duck-typing!
"""
from typing import Protocol

class Barkable(Protocol):
    def bark(self) -> str:
        ...  # New idiom for Abstract / "Won't be defined"

class Corgi():
    # No relation to Barkable at all...
    def bark(self) -> str:
        return "rawrf!"

def trigger_bark(animal: Barkable):
    bark_sound = animal.bark()
    print(f'You hear a "{bark_sound}"')

trigger_bark(Corgi())