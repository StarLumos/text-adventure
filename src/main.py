from __future__ import annotations
from Character import Character
from Location import Location
from Item import Item
from commands.unary import unary

def binary(command: list[str], player: Character):
    if command[0] == "goto":
        if command[1] == player.location.name:
            print("You are already at this location! Try again.")
            return
        for path in player.location.paths:
            if command[1] == path.name:
                player.location = path
                print("You are now at", player.location.name)
                return
        print("Your requested location wasn't found. Try again.")
    elif command[0] == "pickup":
        for item in player.location.items:
            if command[1] == item.name:
                player.items.append(item)
                player.location.items.remove(item)
                print("You have now picked up", item.name, ". It is now in your inventory.")
                return
        print("This item is not in this location. Try again.")
    elif command[0] == "drop":
        for item in player.items:
            if command[1] == item.name:
                player.items.remove(item)
                player.location.items.append(item)
                print("You have now dropped", item.name, ". It is no longer in your inventory.")
                return
        print("You don't have this item in your inventory. Try again.")

def main():
    locationA = Location("Castle", "a brick castle")
    locationB = Location("Garden")
    locationA.paths.append(locationB)
    locationB.paths.append(locationA)
    
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    player = Character(name, [], locationA)
    locationA.characters.append(player)

    itemA = Item("sword", 5000, "uncommon", locationA)
    locationA.items.append(itemA)
    itemB = Item("apple", 5, "common", locationA)
    locationA.items.append(itemB)

    while True:
        command = input("\nEnter your command: ").split(" ")

        if len(command) < 1:
            print("Please enter a command")
            continue
        elif len(command) == 1:
            message, callback = unary(command[0], player)
        else:
            continue # temporary fix
        # elif len(command) == 2:
        #     binary(command, player)
    
        print(message)
        if callback != None:
            callback()
        
    # "attack john sword" (attack john with my sword)

main()