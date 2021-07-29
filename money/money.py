from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Expression(ABC):
    @abstractmethod
    def reduce(self, to: str) -> Money:
        pass

    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Money:
        pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:
        pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression:
        pass


class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend: Expression = augend
        self.addend: Expression = addend

    def reduce(self, bank: Bank, to: str) -> Money:
        amount = (
            self.augend.reduce(bank, to)._amount + self.addend.reduce(bank, to)._amount
        )
        return Money(amount, to)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self.currency: str = currency
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

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self.currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> Money:
        rate = bank.rate(self.currency, to)
        return Money(self._amount / rate, to)


class Bank:
    class Pair:
        def __init__(self, _from: str, to: str) -> None:
            self._from = _from
            self._to = to

        def __eq__(self, object: object) -> bool:
            return self._from == object._from and self._to == object._to

        def __hash__(self) -> int:
            return hash((self._from, self._to))

    def __init__(self):
        self._rates: Dict = dict()

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, _from: str, to: str, rate: int) -> None:
        self._rates[hash(self.Pair(_from, to))] = rate

    def rate(self, _from: str, to: str) -> int:
        if _from == to:
            return 1

        return self._rates[hash(self.Pair(_from, to))]
