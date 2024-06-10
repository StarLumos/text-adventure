from __future__ import annotations
from Time import Time
from Character import Character
from Location import Location
from Item import Item

class Universe:
    time: Time
    characters: list[Character]
    locations: list[Location]
    items: list[Item]
    
    def __init__(self, characters: list[Character] = [], locations: list[Location] = [], items: list[Item] = []):
        self.time = Time()
        self.characters = characters
        self.locations = locations
        self.items = items

    def spawn(self, object: Character | Item, location: Location):
        if type(object) == Character:
            if location not in self.locations:
                raise ValueError(f"Location {location.name} not found in Universe")
            if object in self.characters:
                raise ValueError(f"Character {object.name} already in {location.name}")
            location.characters.append(object)
            self.characters.append(object)
        elif type(object) == Item:
            if location not in self.locations:
                raise ValueError(f"Location {location.name} not found in Universe")
            if object in self.items:
                raise ValueError(f"Item {object.name} already in {location.name}")
            location.items.append(object)
            self.items.append(object)

    def effects(self):
        for character in self.characters:
            for effect in character.effects:
                effect.elapsed += self.time.delta
                if effect.elapsed <= effect.duration:
                    effect.apply()
                else:
                    character.effects.remove(effect)
        
    def update(self):
        self.time.tick()
        self.effects()
