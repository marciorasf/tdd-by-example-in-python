from __future__ import annotations


class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def __eq__(self, object: object) -> bool:
        if isinstance(object, Dollar):
            return self.amount == object.amount

        return False
