from __future__ import annotations


class Money:
    def __init__(self, amount: int) -> None:
        self._amount: int = amount

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Money):
            return self._amount == object._amount and self.__class__ == object.__class__

        return False


class Dollar(Money):
    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
