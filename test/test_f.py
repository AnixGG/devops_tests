"""testing module"""
import my_code.my_functions


def test_plus_plus():
    """test_plus_plus"""
    assert my_code.my_functions.plus_plus(2) == 4
    assert my_code.my_functions.plus_plus(3) == 5
    assert my_code.my_functions.plus_plus(4) == 6
    assert my_code.my_functions.plus_plus(5) == 7


def test_minus_minus():
    """test_minus_minus"""
    assert my_code.my_functions.minus_minus(2) == 0
    assert my_code.my_functions.minus_minus(3) == 1
    assert my_code.my_functions.minus_minus(4) == 2
    assert my_code.my_functions.minus_minus(5) == 3


def test_rock_and_roll():
    """test_rock_and_roll"""
    assert my_code.my_functions.rock_and_roll(1, 1) == "and"
    assert my_code.my_functions.rock_and_roll(133, 5555) == "no no no"
    assert my_code.my_functions.rock_and_roll(13424, 13424) == "and"
    assert my_code.my_functions.rock_and_roll(-1, 0) == "no no no"


def test_is_my_tshirt_size():
    """test_is_my_tshirt_size"""
    assert my_code.my_functions.is_my_tshirt_size(-1)
    assert not my_code.my_functions.is_my_tshirt_size(2)
    assert not my_code.my_functions.is_my_tshirt_size(3)
    assert not my_code.my_functions.is_my_tshirt_size(4)


def test_cm_to_inch():
    """test_cm_to_inch"""
    assert my_code.my_functions.cm_to_inch(1) == 0.393701
    assert my_code.my_functions.cm_to_inch(2) == 0.393701 * 2
    assert my_code.my_functions.cm_to_inch(45) == 0.393701 * 45
    assert my_code.my_functions.cm_to_inch(10) == 0.393701 * 10


def test_multic():
    """test_multic"""
    assert my_code.my_functions.multic(1, 2) == 2
    assert my_code.my_functions.multic(2, 3) == 6
    assert my_code.my_functions.multic(4, 2) == 8
    assert my_code.my_functions.multic(-1, -10) == 10
