from __future__ import annotations


class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def equals(self, dollar: Dollar) -> bool:
        return self.amount == dollar.amount
