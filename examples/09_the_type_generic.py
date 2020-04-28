"""
The covariant Type generic matches Classes (or their children)
"""
from typing import Type

class Pet(): pass
class Dog(Pet): pass
class Chihuahua(Dog): pass

PetSpecies = Type[Pet]

def check_pet(pet: PetSpecies) -> bool:
    return bool(pet)

check_pet(Pet)
check_pet(Chihuahua)
