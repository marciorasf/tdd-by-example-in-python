from __future__ import annotations
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount: int) -> None:
        self._amount: int = amount

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Money):
            return self._amount == object._amount and self.__class__ == object.__class__

        return False

    @staticmethod
    def dollar(amount: int) -> Dollar:
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Franc:
        return Franc(amount)

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass


class Dollar(Money):
    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
