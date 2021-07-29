from __future__ import annotations


class Dollar:
    def __init__(self, amount: int) -> None:
        self._amount: int = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Dollar):
            return self._amount == object._amount

        return False
