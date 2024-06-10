from __future__ import annotations
from Item import Item
import Location
import effects.Effect

class Character:
    name: str
    health: float
    items: list[Item]
    location: Location.Location
    effects: list[effects.Effect.Effect]

    def __init__(self, name: str, items: list[Item], location: Location.Location = Location.ETHER, health: float = 100):
        self.name = name
        self.health = health
        self.items = items
        self.location = location
        self.effects = []


