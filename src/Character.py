from __future__ import annotations
import effects.Effect
import Location
from items.Item import Item
from items.consumables.Consumables import Consumable
from behaviors.Behavior import Behavior
from items.weapons.Weapon import Weapon, WeaponUseResult

class Character:
    name: str
    health: float
    hunger: float
    items: list[Item]
    effects: list[effects.Effect.Effect]
    location: Location.Location

    def __init__(self, name: str, items: list[Item], health: float = 100, hunger: float = 0):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.items = items
        self.location = Location.ETHER
        self.effects = []
    
    def consume(self, item: Consumable):
        item.consume(self)
    
    def attack(self, target: Character, weapon: Weapon, delta: float) -> WeaponUseResult:
        return weapon.use(target, self, delta)

class AICharacter(Character):
    behaviors: list[Behavior]
    def __init__(self, name: str, items: list[Item], health: float = 100, behaviors: list[Behavior] = []):
        super().__init__(name, items, health)
        self.behaviors = behaviors
