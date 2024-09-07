#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
class Dog:
    def __init__(self, breed: str, name: str = "Max"):
        self._name = ""
        self._breed = ""
        self.name = name
        self.breed = breed

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
    
    @property
    def breed(self) -> str:
        return self._breed
    
    @breed.setter
    def breed(self, value: str):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

# Correct instantiation
fido = Dog(breed="Corgi")  # Default name will be "Max"
print(fido.name)  # Output: Max

fido.name = "Effery"
print(fido.name)  # Output: Effery
