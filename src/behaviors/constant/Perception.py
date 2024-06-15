from behaviors.Behavior import Constant
from Character import Character
from items.Item import Item

class Perception(Constant):
    perceived: set[Character | Item]

    def __init__(self):
        self.perceived = set()
    
    def behave(self, subject: Character):
        self.perceived.clear()
        for object in subject.location.characters + subject.location.items:
            if object != subject:
                self.perceived.add(object)
