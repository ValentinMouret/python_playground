"""
Python now has some nice features for type checking.
We can use literals like `list` instead of importing `List` since Python 3.9.
"""

# This import is important to reference the type of the class being created as the return type of the static methods.
from __future__ import annotations

from dataclasses import dataclass
from typing import NewType, Literal

# NewType is a function that creates a new type from an existing type.
# It is useful for type checking and documentation.
OrderId = NewType("OrderId", str)


@dataclass
class Amount:
    amount: int
    # This tells mypy that the currency can only be "EUR" or "USD".
    currency: Literal["EUR", "USD"]


euros_to_dollars = 1.2
dollars_to_euros = 1 / euros_to_dollars


@dataclass
class Euros(Amount):
    amount: int
    currency: str = "EUR"

    def to_dollars(self) -> Dollars:
        return Dollars(int(self.amount * euros_to_dollars))


@dataclass
class Dollars(Amount):
    amount: int
    currency: str = "USD"

    def to_euros(self) -> Euros:
        return Euros(int(self.amount * dollars_to_euros))


Currencies = Dollars | Euros


def convert(amount: Currencies) -> Currencies:
    """
    We can use `is_instance` to check the type of the currencies, even at runtime.
    """
    if isinstance(amount, Euros):
        return amount.to_dollars()
    else:
        return amount.to_euros()


def convert_with_match(amount: Currencies) -> Currencies:
    """
    Pattern matching makes it more readable.
    """
    match amount:
        case Euros(_):
            # Inside match clauses, the type checker knows the type of the variable.
            # So we can call the methods of the class without any problem.
            return amount.to_dollars()
        case Dollars(_):
            return amount.to_euros()
        case _:
            raise ValueError("Unknown currency")
