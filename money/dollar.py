from __future__ import annotations
from money.money import Money


class Dollar(Money):
    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)
