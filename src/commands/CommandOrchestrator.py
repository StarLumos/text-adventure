from commands.Command import Command, Response
from Character import Character
from highlight import yellow

class CommandOrchestrator:
    commands: list[Command]
    player: Character

    def __init__(self, commands: list[Command], player: Character):
        self.commands = commands
        self.player = player
    
    def handle(self, text: str, delta: float) -> Response:
        tokens = text.split(" ")
        
        if len(tokens) == 0:
            return (yellow("Not a valid command! Please try again."), None)
        
        for command in self.commands:
            if command.matches(tokens):
                return command.execute(self.player, tokens, delta)
            
        return (yellow("Not a valid command! Please try again."), None)
