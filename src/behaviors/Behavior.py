from __future__ import annotations
from abc import ABC, abstractmethod
import Character

class Behavior(ABC):
    @abstractmethod
    def behave(self, subject: Character.Character) -> None:
        ...

class Constant(Behavior, ABC):
    ...

class Dormant(Behavior, ABC):
    @abstractmethod
    def trigger(self, subject: Character.Character) -> bool:
        ...
