from commands.Command import Command, Response
from Character import Character
from items.weapons.Weapon import Weapon, WeaponUseResult
from highlight import yellow
from typing import Any, Optional

class Attack(Command):
    def __init__(self):
        super().__init__("attack")
    
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        if len(tokens) < 2:
            return yellow("You must specify a target to attack."), None
        elif len(tokens) < 3:
            return yellow("You must specify a weapon to attack with."), None
        elif len(tokens) > 3:
            return yellow("command usage: attack <target> <weapon>"), None
        
        target = next((
            character for character in player.location.characters if character.name.lower() == tokens[1].lower()), None)
        if target is None:
            return yellow("There is no character nearby with that name."), None

        weapon = next((
            item for item in player.items if item.name.lower() == tokens[2].lower() and isinstance(item, Weapon)), None)
        if weapon is None:
            return yellow("There is no weapon in your inventory with that name."), None

        def battle(offense: tuple[Character, Optional[Weapon]], defense: tuple[Character, Optional[Weapon]], results: list[WeaponUseResult]) -> list[WeaponUseResult]:
            if defense[0].health > 0:
                if offense[1] is None:
                    return battle(defense, offense, results)
                result = offense[0].attack(defense[0], offense[1], delta)
                results.append(result)
                return battle(defense, offense, results)
            else:
                return results

        target_weapon: Any = next(
            filter(lambda i: isinstance(i, Weapon), target.items), None)
        
        results = battle(
            (player, weapon),
            (target, target_weapon),
            []
        )

        message = '\n'.join([ result.message for result in results])

        return message, None
