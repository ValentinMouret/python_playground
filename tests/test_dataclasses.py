from python_playground.dataclasses import User


def test_user_instantiation():
    # The constructor is generated automatically
    user = User("John", 30, "foo@bar.com")
    assert user.name == "John"
    assert user.age == 30
    assert user.email == "foo@bar.com"
    assert user.phone is None
    assert user.is_adult is True


def test_user_equality():
    user = User("John", 30, "foo@bar.com")
    # It comes with equality methods
    user_2 = User("John", 30, "foo@bar.com")
    assert user == user_2


def test_pattern_matching():
    """
    dataclasses are useful for pattern matching.
    It can match even a subset of the fields.

    Note: Pattern matching requires Python 3.10.
    """
    user = User("John", 30, "foo@bar.com")
    match user:
        case User(name="John"):
            assert True
        case _:
            assert False


def test_user_from_dict():
    user = User.from_dict({"name": "John", "age": 30, "email": "foo@bar.com"})
    assert user.name == "John"
    assert user.age == 30
    assert user.email == "foo@bar.com"
    assert user.phone is None
    assert user.is_adult is True


def test_user_from_record():
    user = User.from_record(("John", 30, "foo@bar.com"))
    assert user.name == "John"
    assert user.age == 30
    assert user.email == "foo@bar.com"
    assert user.phone is None
    assert user.is_adult is True
