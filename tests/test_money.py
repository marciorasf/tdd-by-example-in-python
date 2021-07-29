from __future__ import annotations
from money.money import Bank, Money, Sum


def test_dollar_multiplication():
    five = Money.dollar(5)

    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) != Money.dollar(5)


def test_currency():
    assert Money.dollar(1).currency == "USD"
    assert Money.franc(1).currency == "CHF"


def test_simple_addition():
    five = Money.dollar(5)
    money_sum = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(money_sum, "USD")
    assert reduced == Money.dollar(10)


def test_plus_returns_sum():
    five = Money.dollar(5)
    money_sum: Sum = five.plus(five)

    assert money_sum.augend == five
    assert money_sum.augend == five


def test_reduce_sum():
    money_sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(money_sum, "USD")
    assert result == Money.dollar(7)


def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert result == Money.dollar(1)
