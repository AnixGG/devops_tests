import pytest
from my_code.my_functions import *


@pytest.mark.parametrize(
    "a, rez", [
        (2, 4),
        (3, 5),
        (4, 6),
        (6, 8),
        (32, 34),
        (4343, 4345),
    ]
)
def test_plus_plus(a, rez):
    assert plus_plus(a) == rez


@pytest.mark.parametrize(
    "rez, a", [
        (2, 0),
        (3, 1),
        (4, 2),
        (6, 4),
        (32, 30),
        (4343, 4341),
    ]
)
def test_minus_minus(rez, a):
    assert plus_plus(a) == rez


@pytest.mark.parametrize(
    "a, b, rez", [
        (1, 1, "and"),
        (1, 0, "no no no"),
        (10, -340, "no no no"),
        (133, 5555, "no no no"),
        (13424, 13424, "and"),
        (25232, 23434, "no no no"),
        (2345, 7627573, "no no no"),
    ]
)
def rock_and_roll(a, b, rez):
    assert rock_and_roll(a, b) == rez


@pytest.mark.parametrize(
    "a, rez", [
        (-1, True),
        (2, False),
        (3, False),
        (4, False),
        (6, False),
        (32, False),
        (4343, False),
    ]
)
def test_is_my_tshirt_size(a, rez):
    assert is_my_tshirt_size(a) == rez


@pytest.mark.parametrize(
    "a, rez", [
        (1, 0.393701),
        (2, 2 * 0.393701),
        (45, 45 * 0.393701),
        (10, 10 * 0.393701),
        (12, 12 * 0.393701),
        (-10, -10 * 0.393701),
    ]
)
def test_cm_to_inch(a, rez):
    assert cm_to_inch(a) == rez


@pytest.mark.parametrize(
    "a, b, rez", [
        (1, 1, 1),
        (5, 2, 10),
        (1, 3, 3),
        (2, 45, 90),
        (56, 0, 0),
        (-1, 23, -23),
        (23, 1, 23),
    ]
)
def test_multic(a, b, rez):
    assert multic(a, b) == rez
