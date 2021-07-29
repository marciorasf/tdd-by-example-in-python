from money.dollar import Dollar


def test_multiplication():
    five = Dollar(5)
    five.times(2)
    five.amount == 10
