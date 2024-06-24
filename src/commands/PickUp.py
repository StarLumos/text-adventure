from commands.Command import Command, Response
from Character import Character

class PickUp(Command):
    def __init__(self):
        super().__init__("pickup")
    
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        for item in player.location.items:
            if tokens[1].lower() == item.name.lower():
                player.items.append(item)
                player.location.items.remove(item)
                return "You have now picked up " + item.name + ". It is now in your inventory.", None
        return "This item is not in this location. Try again.", None
