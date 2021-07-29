from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Expression(ABC):
    @abstractmethod
    def reduce(self, to: str) -> Money:
        pass

    def reduce(self, bank: Bank, to: str) -> Money:
        pass


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to: str) -> Money:
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

    def reduce(self, bank: Bank, to: str):
        rate = bank.rate(self.currency, to)
        return Money(self._amount / rate, to)


class Bank:
    class Pair:
        def __init__(self, source: str, to: str) -> None:
            self._from = source
            self._to = to

        def __eq__(self, object: object) -> bool:
            return self._from == object._from and self._to == object._to

        def __hash__(self) -> int:
            return hash((self._from, self._to))

    def __init__(self):
        self._rates: Dict = dict()

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, source: str, to: str, rate: int) -> None:
        self._rates[hash(self.Pair(source, to))] = rate

    def rate(self, source: str, to: str) -> int:
        if source == to:
            return 1

        return self._rates[hash(self.Pair(source, to))]
