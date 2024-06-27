from commands.Command import Command, Response
from Character import Character
from highlight import black

class Exit(Command):
    def __init__(self):
        super().__init__("exit")
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        return (black("You are now exiting the game. Thank you for playing!"), quit)
