from .Command import Command, Response
from ..Character import Character

class CommandOrchestrator:
    commands: list[Command]
    player: Character

    def __init__(self, commands: list[Command], player: Character):
        self.commands = commands
        self.player = player
    
    def handle(self, text: str) -> Response:
        tokens = text.split(" ")
        if len(tokens) == 0:
            return ("Not a valid command! Please try again.", None)
        for command in self.commands:
            if command.matches(tokens[0]):
                return command.execute(self.player)
        return ("Not a valid command! Please try again.", None)
