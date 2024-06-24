from __future__ import annotations
from Character import Character
from abc import ABC, abstractmethod

from typing import TypeAlias, Callable, Any

Callback: TypeAlias = Callable[[], Any]
Response: TypeAlias = tuple[str, Callback | None]

class Command(ABC):
    keyword: str

    def __init__(self, keyword: str):
        self.keyword = keyword

    def matches(self, tokens: list[str]) -> bool:
        return tokens[0].lower() == self.keyword.lower()

    @abstractmethod
    def execute(self, player: Character, tokens: list[str], delta: float) -> Response:
        ...
