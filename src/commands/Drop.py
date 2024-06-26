from commands.Command import Command, Response
from Character import Character
from highlight import red, yellow

class Drop(Command):
    def __init__(self):
        super().__init__("drop")
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        for item in player.items:
            if tokens[1].lower() == item.name.lower():
                player.items.remove(item)
                player.location.items.append(item)
                return red(f'- {item.name}'), None
        return red("You don't have this item in your inventory. Try again."), None
