from __future__ import annotations
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def reduce(self, to: str) -> Money:
        pass


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Money:
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self.currency = currency
        self._amount: int = amount

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Money):
            return self._amount == object._amount and self.currency == object.currency

        return False

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self.currency)

    def plus(self, addend: Money) -> Expression:
        return Sum(self, addend)

    def reduce(self, to: str):
        return self


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(to)
