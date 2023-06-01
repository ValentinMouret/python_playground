from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

"""
Dataclasses are a way to create classes that are meant to store data.
They are akin to structs in C, but with added functionality.
"""


@dataclass
class User:
    name: str
    age: int
    email: str

    # Some fields can be optional
    phone: Optional[str] = None

    # Some fields can be generated once the object is created
    # They have to be initialised in the `__post_init__` method.
    is_adult: bool = field(init=False)

    def __post_init__(self):
        self.is_adult = self.age >= 18

    # It can have regular methods
    def greet(self):
        print(f"Hello {self.name}!")

    @staticmethod
    def from_dict(data: dict):
        """
        It can be useful to add static methods to dataclasses to make it easier
        to instantiate them from other data structures.
        """
        return User(data["name"], data["age"], data["email"])

    @staticmethod
    def from_record(record: tuple) -> User:
        """
        Assumes that the record is a tuple of the form (name, age, email).
        """
        name, age, email = record
        return User(name, age, email)


"""
This is essentially equivalent to the following (minus the static methods):

class User:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self) -> str:
        return f"User(name={self.name}, age={self.age}, email={self.email})"

    def __eq__(self, other: User) -> bool:
        return (
            self.name == other.name
            and self.age == other.age
            and self.email == other.email
        )

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash((self.name, self.age, self.email))

"""
