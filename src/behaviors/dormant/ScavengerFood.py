from behaviors.Behavior import Dormant
from Character import Character
from items.consumables.Food import Food

class ScavengeFood(Dormant):
    def trigger(self, subject: Character) -> bool:
        return subject.health < 30
    
    def behave(self, subject: Character): 
        food = next(
            (item for item in subject.items if isinstance(item, Food)), None)
        if food:
            subject.consume(food)
            print(f"{subject.name} ate {food.name}")
            print(f"new health: {subject.health}") 
        else:
            print(f"{subject.name} has no food!!")
        


        # if I dont have food. go look in the room.
        # if the room has no food, go to another room.

        # if health drops below 15, make me go into a panic induced state.