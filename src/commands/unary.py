from __future__ import annotations
from Character import Character

# imperative version, mostly pure but does contain local mutation to response
def who(player: Character) -> str:
    response = ""
    if len(player.location.characters) == 1:
        response = "There are no other characters at this location."
    else:
        response = "These characters are nearby:"
        for character in player.location.characters:
            if character != player:
                response += "-" + character.name
    return response

# example of a 100% pure function, using an expressive/declarative 1-liner style 
# def who(player: Character) -> str:
#     return "There are no other characters at this location." if len(player.location.characters) == 1 else "These characters are nearby:" + ", ".join(
#         [ character.name for character in player.location.characters if character != player])

def where(player: Character) -> str:
    response = "You are at " + player.location.name
    if player.location.description != " ":
        response += "\n" + player.location.name + " is " + player.location.description
    
    if player.location.paths == []:
        response += "\nThere are no connecting paths to this location."
    else:
        response += "\n" + player.location.name + " is connected to " + " ".join(
            [ path.name for path in player.location.paths ])
    return response

def inv(player: Character) -> str:
    response = "Your inventory:"
    if player.items == []:
        response += "\nYou have no items."
    else:
        for item in player.items:
            response += "-" + item.name
    return response

def me(player: Character) -> str:
    response = "Your name is " + player.name
    response += "\nYour health is " + str(player.health)
    if player.items == []:
        response += "\nYou have no items."
    else:
        response += "\nYour item(s) is/are " + " ".join(
            [ item.name for item in player.items])
    response += "\nYour location is " + player.location.name
    return response

def exit() -> str:
    return "You are now exiting the game. Thank you for playing!"
    quit()

def unary(command: str, player: Character) -> str: 
    result: str
    match command: 
        case "who":
            result = who(player)
        case "where":
            result = where(player)
        case "inv":
            result = inv(player)
        case "me":
            result = me(player)
        case "exit":
            result = exit()
        case _:
            result = "Invalid command. Please try again."

    return result