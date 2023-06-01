from python_playground.typing import Euros, Dollars, convert, convert_with_match


def test_convert():
    euros = Euros(100)
    assert convert(euros) == Dollars(120)


def test_convert_with_match():
    dollars = Dollars(100)
    assert convert_with_match(dollars) == Euros(83)
