from __future__ import annotations
from Time import Time
from Character import AICharacter, Character
from behaviors.Behavior import Dormant
from Location import Location
from items.Item import Item

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

    def spawn(self, obj: Character | Item, location: Location):
        if isinstance(obj, Character):
            if location not in self.locations:
                raise ValueError(f"Location {location.name} not found in Universe")
            if obj in self.characters:
                raise ValueError(f"Character {obj.name} already in {location.name}")
            location.characters.append(obj)
            self.characters.append(obj)
        else:
            if location not in self.locations:
                raise ValueError(f"Location {location.name} not found in Universe")
            if obj in self.items:
                raise ValueError(f"Item {obj.name} already in {location.name}")
            location.items.append(obj)
            self.items.append(obj)
        obj.location = location

    def effects(self):
        for character in self.characters:
            for effect in character.effects:
                effect.elapsed += self.time.delta
                if effect.elapsed <= effect.duration:
                    effect.apply()
                else:
                    character.effects.remove(effect)

    def behaviors(self):
        for character in self.characters:
            if isinstance(character, AICharacter):
                for behavior in character.behaviors:
                    if isinstance(behavior, Dormant):
                        if behavior.trigger(character):
                            behavior.behave(character)
                    else:
                        behavior.behave(character)

    def update(self):
        self.time.tick()
        self.effects()
        self.behaviors()
