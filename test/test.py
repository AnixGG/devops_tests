from my_code.my_functions import *


def test_plus_plus():
    assert plus_plus(2) == 4
    assert plus_plus(3) == 5
    assert plus_plus(4) == 6
    assert plus_plus(5) == 7


def test_minus_minus():
    assert plus_plus(2) == 0
    assert plus_plus(3) == 1
    assert plus_plus(4) == 2
    assert plus_plus(5) == 3


def test_rock_and_roll():
    assert rock_and_roll(1, 1) == "and"
    assert rock_and_roll(133, 5555) == "no no no"
    assert rock_and_roll(13424, 13424) == "and"
    assert rock_and_roll(-1, 0) == "no no no"


def test_is_my_tshirt_size():
    assert is_my_tshirt_size(-1) == True
    assert is_my_tshirt_size(2) == False
    assert is_my_tshirt_size(3) == False
    assert is_my_tshirt_size(4) == False


def test_cm_to_inch():
    assert cm_to_inch(1) == 0.393701
    assert cm_to_inch(2) == 0.393701 * 2
    assert cm_to_inch(45) == 0.393701 * 45
    assert cm_to_inch(10) == 0.393701 * 10


def test_multic():
    assert multic(1, 2) == 2
    assert multic(2, 3) == 6
    assert multic(4, 2) == 8
    assert multic(-1, -10) == 10
