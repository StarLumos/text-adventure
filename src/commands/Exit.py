from commands.Command import Command, Response
from Character import Character

class Exit(Command):
    def __init__(self):
        super().__init__("exit")
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        return ("You are now exiting the game. Thank you for playing!", quit)
