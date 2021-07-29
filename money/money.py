from __future__ import annotations
from abc import ABC, abstractmethod


class Money:
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
