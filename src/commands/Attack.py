from commands.Command import Command, Response
from Character import Character
from items.weapons.Weapon import Weapon

class Attack(Command):
    def __init__(self):
        super().__init__("attack")
    
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        if len(tokens) < 2:
            return "You must specify a target to attack.", None
        elif len(tokens) < 3:
            return "You must specify a weapon to attack with.", None
        elif len(tokens) > 3:
            return "command usage: attack <target> <weapon>", None
        
        target = next((
            character for character in player.location.characters if character.name.lower() == tokens[1].lower()), None)
        if target is None:
            return "There is no character nearby with that name.", None

        weapon = next((
            item for item in player.items if item.name.lower() == tokens[2].lower() and isinstance(item, Weapon)), None)
        if weapon is None:
            return "There is no weapon in your inventory with that name.", None
        
        return player.attack(target, weapon, delta).message, None
