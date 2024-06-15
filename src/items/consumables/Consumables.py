from __future__ import annotations
from abc import abstractmethod
from items.Item import Item
import Character

class Consumable(Item):
    @abstractmethod
    def consume(self, subject: Character.Character): 
        ...
