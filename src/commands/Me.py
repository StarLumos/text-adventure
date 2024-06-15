from commands.Command import Command, Response
from Character import Character

class Me(Command):
    def __init__(self):
        super().__init__("me")
    
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        message = "Name: " + player.name
        message += "\nHealth: " + str(player.health)
        if player.items == []:
            message += "\nYou have no items."
        else:
            message += "\nItems: \n - " + "\n - ".join(
                [ item.name for item in player.items])
        message += "\nLocation: " + player.location.name
        return message, None
