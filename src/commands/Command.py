from __future__ import annotations
from Character import Character
from abc import ABC, abstractmethod

from typing import TypeAlias, Callable, Any

Callback: TypeAlias = Callable[[], Any]
Response: TypeAlias = tuple[str, Callback | None]

class Command(ABC):
    keyword: str

    def __init__(self, keyword: str):
        self.keyword = keyword

    def matches(self, tokens: list[str]) -> bool:
        return tokens[0] == self.keyword

    @abstractmethod
    def execute(self, player: Character, tokens: list[str]) -> Response:
        ...


class WhoCommand(Command):
    def __init__(self):
        super().__init__("who")
    
    def execute(self, player: Character, tokens: list[str]) -> Response:
        message = ""
        if len(player.location.characters) == 1:
            message = "There are no other characters at this location."
        else:
            message = "These characters are nearby:"
            for character in player.location.characters:
                if character != player:
                    message += "-" + character.name
        return message, None

class WhereCommand(Command):
    def __init__(self):
        super().__init__("where")

    def execute(self, player: Character, tokens: list[str]) -> Response:
        message = "You are at " + player.location.name
        if player.location.description != " ":
            message += "\n" + player.location.name + " is " + player.location.description
        
        if player.location.paths == []:
            message += "\nThere are no connecting paths to this location."
        else:
            message += "\n" + player.location.name + " is connected to " + " ".join(
                [ path.name for path in player.location.paths ])
        return message, None

class InvCommand(Command):
    def __init__(self):
        super().__init__("inv")
    
    def execute(self, player: Character, tokens: list[str]) -> Response:
        message = "Your inventory:"
        if player.items == []:
            message += "\nYou have no items."
        else:
            for item in player.items:
                message += "\n- " + item.name
        return message, None



class MeCommand(Command):
    def __init__(self):
        super().__init__("me")
    
    def execute(self, player: Character, tokens: list[str]) -> Response:
        message = "Name: " + player.name
        message += "\nHealth: " + str(player.health)
        if player.items == []:
            message += "\nYou have no items."
        else:
            message += "\nItems: \n - " + "\n - ".join(
                [ item.name for item in player.items])
        message += "\nLocation: " + player.location.name
        return message, None

class ExitCommand(Command):
    def __init__(self):
        super().__init__("exit")
    def execute(self, player: Character, tokens: list[str]) -> Response:
        return ("You are now exiting the game. Thank you for playing!", quit)

class GoToCommand(Command):
    def __init__(self):
        super().__init__("goto")

    def execute(self, player: Character, tokens: list[str] = []) -> Response:
        if tokens[1].lower() == player.location.name.lower():
            return "You are already at this location! Try again.", None
        for path in player.location.paths:
            if tokens[1].lower() == path.name.lower():
                player.location = path
                return "You are now at " + player.location.name, None
        return "Your requested location wasn't found. Try again.", None

class PickUpCommand(Command):
    def __init__(self):
        super().__init__("pickup")
    
    def execute(self, player: Character, tokens: list[str] = []) -> Response:
        for item in player.location.items:
            if tokens[1] == item.name:
                player.items.append(item)
                player.location.items.remove(item)
                return "You have now picked up " + item.name + ". It is now in your inventory.", None
        return "This item is not in this location. Try again.", None

class DropCommand(Command):
    def __init__(self):
        super().__init__("drop")
    def execute(self, player: Character, tokens: list[str] = []) -> Response:
        for item in player.items:
            if tokens[1] == item.name:
                player.items.remove(item)
                player.location.items.append(item)
                return "You have now dropped " + item.name + ". It is no longer in your inventory.", None
        return "You don't have this item in your inventory. Try again.", None
