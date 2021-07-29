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


def test_reduce_money_different_currency():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert result == Money.dollar(1)


def test_identity_rate():
    assert Bank().rate("USD", "USD") == 1


def test_mixed_addition():
    five_dollars = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(five_dollars.plus(ten_francs), "USD")
    assert result == Money.dollar(10)


def test_sum_plus_money():
    five_dollars = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    money_sum = Sum(five_dollars, ten_francs).plus(five_dollars)
    result = bank.reduce(money_sum, "USD")
    assert result == Money.dollar(15)


def test_sum_times():
    five_dollars = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    money_sum = Sum(five_dollars, ten_francs).times(2)
    result = bank.reduce(money_sum, "USD")
    assert result == Money.dollar(20)
