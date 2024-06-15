from behaviors.Behavior import Constant
from Character import Character

class Hunger(Constant):    
    def behave(self, subject: Character):
        if subject.hunger < 100:
            subject.hunger += 0.1
    
        if subject.hunger >= 100:
            subject.health -= 5