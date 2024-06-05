from __future__ import annotations
import Character
import Item

class Location:
    name: str
    description: str
    characters: list[Character.Character]
    items: list[Item.Item]
    paths: list[Location]
    
    def __init__(self, name: str, description: str = " "):
        self.name = name
        self.description = description
        self.characters = []
        self.items = []
        self.paths = []
    