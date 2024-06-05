from __future__ import annotations
from Item import Item
import Location

class Character:
    name: str
    health: float
    items: list[Item]
    location: Location.Location

    def __init__(self, name: str, items: list[Item], location: Location.Location, health: float = 100):
        self.name = name
        self.health = health
        self.items = items
        self.location = location
