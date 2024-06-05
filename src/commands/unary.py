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
        response += player.location.name + " is " + player.location.description
    
    if player.location.paths == []:
        response += "There are no connecting paths to this location."
    else:
        response += player.location.name + "is connected to" + " ".join(
            [ path.name for path in player.location.paths ])
    return response

def inv(player: Character) -> str:
    response = "Your inventory:"
    if player.items == []:
        response += "You have no items."
    else:
        for item in player.items:
            response += "-" + item.name
    return response

def me(player: Character) -> str:
    response = "Your name is " + player.name
    response += "Your health is " + str(player.health)
    if player.items == []:
        response += "You have no items."
    else:
        response += "Your item(s) is/are " + " ".join(
            [ item.name for item in player.items])
    response += "Your location is " + player.location.name
    return response

def exit():
    return "You are now exiting the game. Thank you for playing!"
    quit()

def unary(command: str, player: Character): 
    match command: 
        case "who":
            who(player)
        case "where":
            where(player)
        case "inv":
            inv(player)
        case "me":
            me(player)
        case "exit":
            exit()
        case _:
            print("Invalid command. Please try again.")