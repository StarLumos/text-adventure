from commands.Command import Command, Response
from Character import Character
from highlight import yellow, black, white

class GoTo(Command):
    def __init__(self):
        super().__init__("goto")

    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        if tokens[1].lower() == player.location.name.lower():
            return yellow("You are already at this location! Try again."), None
        for path in player.location.paths:
            if tokens[1].lower() == path.name.lower():
                player.location = path
                return black("You are now at ") + white(player.location.name), None
        return yellow("Your requested location wasn't found. Try again."), None
