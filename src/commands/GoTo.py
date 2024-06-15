from commands.Command import Command, Response
from Character import Character

class GoTo(Command):
    def __init__(self):
        super().__init__("goto")

    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        if tokens[1].lower() == player.location.name.lower():
            return "You are already at this location! Try again.", None
        for path in player.location.paths:
            if tokens[1].lower() == path.name.lower():
                player.location = path
                return "You are now at " + player.location.name, None
        return "Your requested location wasn't found. Try again.", None
