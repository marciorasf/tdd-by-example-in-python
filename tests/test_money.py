from money.money import Money


def test_dollar_multiplication():
    five = Money.dollar(5)

    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) == Money.franc(5)
    assert Money.franc(5) != Money.franc(6)
    assert Money.franc(5) != Money.dollar(5)


def test_franc_multiplication():
    five = Money.franc(5)

    assert Money.franc(10) == five.times(2)
    assert Money.franc(15) == five.times(3)


def test_currency():
    assert Money.dollar(1).currency == "USD"
    assert Money.franc(1).currency == "CHF"


def test_different_class_equality():
    assert Money(10, "CHF") == Money.franc(10)
