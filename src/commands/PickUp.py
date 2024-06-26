from commands.Command import Command, Response
from Character import Character
from highlight import blue, yellow, green, white, red

class PickUp(Command):
    def __init__(self):
        super().__init__("pickup")
    
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        for item in player.location.items:
            if tokens[1].lower() == item.name.lower():
                player.items.append(item)
                player.location.items.remove(item)
                return green(f'+ {item.name}') + ' - ' + white(item.description), None
                # return green("You have now picked up ") + blue(item.name) + green(". It is now in your inventory."), None
        return red("This item is not in this location. Try again."), None
