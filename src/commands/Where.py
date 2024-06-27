from commands.Command import Command, Response
from Character import Character
from highlight import black, white, yellow

class Where(Command):
    def __init__(self):
        super().__init__("where")

    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        message = black("You are at ") + white(player.location.name)
        if player.location.description != " ":
            message += "\n" + white(player.location.name) + black(" is ") + white(player.location.description)
        
        if player.location.paths == []:
            message += yellow("\nThere are no connecting paths to this location.")
        else:
            message += "\n" + white(player.location.name) + black(" is connected to ") + " ".join(
                [ white(path.name) for path in player.location.paths ])
        return message, None
