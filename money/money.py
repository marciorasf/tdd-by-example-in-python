from __future__ import annotations
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount: int, currency: str) -> None:
        self.currency = currency
        self._amount: int = amount

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Money):
            return self._amount == object._amount and self.__class__ == object.__class__

        return False

    @staticmethod
    def dollar(amount: int) -> Dollar:
        return Dollar(amount, None)

    @staticmethod
    def franc(amount: int) -> Franc:
        return Franc(amount, None)

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass


class Dollar(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, "USD")

    def times(self, multiplier: int) -> Money:
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, "CHF")

    def times(self, multiplier: int) -> Money:
        return Money.franc(self._amount * multiplier)
