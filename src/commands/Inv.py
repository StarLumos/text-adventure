from commands.Command import Command, Response
from Character import Character

class Inv(Command):
    def __init__(self):
        super().__init__("inv")
    
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        message = "Your inventory:"
        if player.items == []:
            message += "\nYou have no items."
        else:
            for item in player.items:
                message += "\n- " + item.name
        return message, None
