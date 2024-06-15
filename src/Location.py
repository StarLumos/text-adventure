from __future__ import annotations
import Character
import items.Item as Item

class Location:
    name: str
    description: str
    characters: list[Character.Character]
    items: list[Item.Item]
    paths: list[Location]
    
    def __init__(self, name: str, description: str, characters: list[Character.Character], items: list[Item.Item], paths: list[Location]):
        self.name = name
        self.description = description
        self.characters = characters
        self.items = items
        self.paths = paths
    
ETHER = Location("the Ether", "a place nowhere and everywhere", [], [], [])
