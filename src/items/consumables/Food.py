from items.consumables.Consumables import Consumable
from items.Item import Rarity
import Character

class Food(Consumable):
    healthpoints: int

    def __init__(self, name: str, worth: float, rarity: Rarity, healthpoints: int):
        super().__init__(name, worth, rarity)
        self.healthpoints = healthpoints

    def consume(self, subject: Character.Character):
        subject.health += self.healthpoints

class Chicken(Food):
    def __init__(self):
        super().__init__('Chicken', 10, 'common', 5)
