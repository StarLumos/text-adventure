from typing import Literal, TypeAlias
from Location import Location

Rarity: TypeAlias = Literal['common', 'uncommon', 'rare', 'legendary']

class Item:
    name: str
    worth: float
    rarity: Rarity
    location: Location

    def __init__(self, name: str, worth: float, rarity: Rarity, location: Location):
        self.name = name
        self.worth = worth
        self.rarity = rarity
        self.location = location
