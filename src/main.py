from __future__ import annotations
from Universe import Universe
from Character import Character
from Location import Location
from Item import Item
from commands.CommandOrchestrator import CommandOrchestrator
from commands.Command import WhoCommand, WhereCommand, InvCommand, MeCommand, GoToCommand, ExitCommand, PickUpCommand, DropCommand
from effects.Effect import Burning

def main():
    universe = Universe()
    locationA = Location("the Castle", "a brick castle")
    locationB = Location("the Garden")
    locationA.paths.append(locationB)
    locationB.paths.append(locationA)
    universe.locations.append(locationA)
    universe.locations.append(locationB)
    
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    player = Character(name, [])
    universe.spawn(player, locationA)
    itemA = Item("sword", 5000, "uncommon", locationA)
    universe.spawn(itemA, locationA)
    itemB = Item("apple", 5, "common", locationA)
    universe.spawn(itemB, locationA)
    
    orchestrator = CommandOrchestrator([
        WhoCommand(), 
        WhereCommand(), 
        InvCommand(), 
        MeCommand(), 
        ExitCommand(), 
        GoToCommand(), 
        PickUpCommand(),
        DropCommand(),
    ], player)

    effect = Burning(10, player)
    player.effects.append(effect)

    while True:
        text = input("\nEnter your command: ")
        message, callback = orchestrator.handle(text)
        
        universe.update()
        
        print(message)
        if callback is not None:
            callback()
        
    # "attack john sword" (attack john with my sword)

main()
