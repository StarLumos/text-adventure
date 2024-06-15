from __future__ import annotations
from Universe import Universe
from Character import Character, AICharacter
from behaviors.constant.Perception import Perception
from behaviors.dormant.ScavengerFood import ScavengeFood
from Location import Location
from items.Item import Item
from commands.CommandOrchestrator import CommandOrchestrator
from commands.Who import Who
from commands.Where import Where
from commands.Inv import Inv
from commands.Me import Me
from commands.GoTo import GoTo
from commands.PickUp import PickUp
from commands.Drop import Drop
from commands.Exit import Exit
from commands.Attack import Attack
from effects.Effect import Burning
from items.weapons.Weapon import Sword

def main():
    universe = Universe()
    locationA = Location("Castle", "a brick castle", [], [], [])
    locationB = Location("Garden", "", [], [], [])
    locationA.paths.append(locationB)
    locationB.paths.append(locationA)
    universe.locations.append(locationA)
    universe.locations.append(locationB)
    
    name = input("Enter your name: ")
    player = Character(name, [])
    print(f"Hello, {name}")

    universe.spawn(player, locationA)
    itemA = Sword("excalibur", 5000, "uncommon", 10, 3, 94)
    universe.spawn(itemA, locationA)
    itemB = Item("apple", 5, "common")
    universe.spawn(itemB, locationA)

    npc = AICharacter("Enchantress", [], 20, [ Perception(), ScavengeFood() ])
    universe.spawn(npc, locationA)

    orchestrator = CommandOrchestrator([
        Who(), 
        Where(), 
        Inv(), 
        Me(), 
        Exit(), 
        GoTo(), 
        PickUp(),
        Drop(),
        Attack()
    ], player)

    effect = Burning(10, player)
    player.effects.append(effect)

    while True:
        text = input("\nEnter your command: ")
        message, callback = orchestrator.handle(text, universe.time.delta)

        universe.update()
        
        print(message)
        npc.health = 15
        if callback is not None:
            callback()

main()
