from __future__ import annotations
from items.Item import Item, Rarity
from abc import ABC, abstractmethod
import Character
from random import randrange
from typing import NamedTuple
from highlight import black, red, yellow, blue, magenta

class WeaponUseResult(NamedTuple):
    used: bool
    hit: bool
    damage: float
    message: str

class Weapon(Item, ABC):
    damage: float
    cooldown: float
    timer: float
    accuracy: float

    def __init__(self, name: str, worth: float, rarity: Rarity, damage: float, cooldown: float, accuracy: float):
        super().__init__(name, worth, rarity)
        self.damage = damage
        self.cooldown = cooldown
        self.timer = 0
        self.accuracy = accuracy
    
    @abstractmethod
    def use(self, target: Character.Character, user: Character.Character, delta: float) -> WeaponUseResult:
        ...

class Sword(Weapon):
    def __init__(self, name: str, worth: float, rarity: Rarity, damage: float, cooldown: float, accuracy: float):
        super().__init__(name, worth, rarity, damage, cooldown, accuracy)
    
    def use(self, target: Character.Character, user: Character.Character, delta: float) -> WeaponUseResult:
        self.timer -= delta
        if self.timer > 0:
            return WeaponUseResult(
                False, False, 0, yellow("This weapon is on cooldown."))
        else:
            self.timer = self.cooldown
    
        chance = randrange(0, 100)
        if chance <= self.accuracy:
            target.health -= self.damage
            message = blue(f"{user.name}") + black("dealt ") + magenta(f"{self.damage} damage ") + black("to ") + blue(target.name) + black("!\n\t") + magenta(target.health + self.damage) + magenta("hp -> ") + magenta(target.health) + magenta("hp")
            if target.health <= 0:
                message += "\n" + blue(target.name) + black(" has died! You've won the battle!")
            if user.health <= 0:
                message += "\n" + black("You've ") +  red("died ") +  black("and lost the battle.")
            return WeaponUseResult(
                True, True, self.damage, message)
        else:
            return WeaponUseResult(
                True, False, 0, yellow("This weapon missed the target."))

class Dagger(Weapon):
    ...

class Crossbow:
    ...

class Staff:
    ...
