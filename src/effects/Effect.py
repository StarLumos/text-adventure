from __future__ import annotations
from abc import ABC, abstractmethod
import Character

class Effect(ABC):
    name: str
    duration: float
    elapsed: float
    recipient: Character.Character

    def __init__(self, name: str, duration: float, recipient: Character.Character):
        self.name = name
        self.duration = duration
        self.elapsed = 0
        self.recipient = recipient
    
    @abstractmethod
    def apply(self): ...

class Burning(Effect):
    def __init__(self, elapsed: float, recipient: Character.Character):
        super().__init__("Burning!", elapsed, recipient)
    
    def apply(self):
        self.recipient.health -= 10

# class Healing(Effect):
#     def __init__(self, elapsed: float, recipient: Character):
#         super().__init__("Healing!", elapsed, recipient)
    
#     def apply(self):
#         self.recipient.items = 

# class Impoverate(Effect):
#     def __init__(self, elapsed: float, recipient: Character):
#         super().__init__("Impover")