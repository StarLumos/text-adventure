from commands.Command import Command, Response
from Character import Character
from highlight import black, blue

class Who(Command):
    def __init__(self):
        super().__init__("who")
    
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        message = ""
        if len(player.location.characters) == 1:
            message = black("There are no other characters at this location.")
        else:
            message = black("These characters are nearby:")
            for character in player.location.characters:
                if character != player:
                    message += black("\n - ") + blue(character.name)
        return message, None
