from commands.Command import Command, Response
from Character import Character

class Where(Command):
    def __init__(self):
        super().__init__("where")

    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        message = "You are at " + player.location.name
        if player.location.description != " ":
            message += "\n" + player.location.name + " is " + player.location.description
        
        if player.location.paths == []:
            message += "\nThere are no connecting paths to this location."
        else:
            message += "\n" + player.location.name + " is connected to " + " ".join(
                [ path.name for path in player.location.paths ])
        return message, None
