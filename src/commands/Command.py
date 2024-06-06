from __future__ import annotations
from Character import Character
from abc import ABC, abstractmethod

from typing import Callable, Any, TypeAlias

Callback: TypeAlias = Callable[[], Any]
Response: TypeAlias = tuple[str, Callback | None]

class Command(ABC):
    keyword: str

    def __init__(self, keyword: str):
        self.keyword = keyword

    def matches(self, message: str) -> bool:
        return message == self.keyword

    @abstractmethod
    def execute(self, player: Character) -> Response:
        ...

class WhoCommand(Command):
    def __init__(self):
        super().__init__("who")
    
    def execute(self, player: Character) -> Response:
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

    def execute(self, player: Character) -> Response:
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
    
    def execute(self, player: Character) -> Response:
        message = "Your inventory:"
        if player.items == []:
            message += "\nYou have no items."
        else:
            for item in player.items:
                message += "-" + item.name
        return message, None

class MeCommand(Command):
    def __init__(self):
        super().__init__("me")
    
    def execute(self, player: Character) -> Response:
        message = "Your name is " + player.name
        message += "\nYour health is " + str(player.health)
        if player.items == []:
            message += "\nYou have no items."
        else:
            message += "\nYour item(s) is/are " + " ".join(
                [ item.name for item in player.items])
        message += "\nYour location is " + player.location.name
        return message, None

class ExitCommand(Command):
    def __init__(self):
        super().__init__("help")
    def execute(self, player: Character) -> Response:
        return ("You are now exiting the game. Thank you for playing!", quit)
