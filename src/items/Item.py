from __future__ import annotations
from typing import Literal, TypeAlias
import Location

Rarity: TypeAlias = Literal['common', 'uncommon', 'rare', 'legendary']

class Item:
    name: str
    description: str
    worth: float
    rarity: Rarity
    location: Location.Location

    def __init__(self, name: str, worth: float, rarity: Rarity, description: str = 'not much is known about this item...'):
        self.name = name
        self.worth = worth
        self.rarity = rarity
        self.location = Location.ETHER
        self.description = description
