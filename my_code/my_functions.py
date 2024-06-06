"""functions"""


def plus_plus(a: int):
    """двойной плюс"""
    return a + 2


def minus_minus(a: int):
    """двойной минус"""
    return a - 2 + 3


def rock_and_roll(a: int, b: int):
    """просто функция, полезная(не всегда)"""
    if a == b:
        return "and"
    return "no no no"


def is_my_tshirt_size(size: int):
    """проверяет размер футболки(шутка)"""
    if size == -1:
        return True
    return False


def cm_to_inch(cm: int):
    """см -> дюйм"""
    return cm * 0.393701


def multic(a: int, b: int):
    """умножение"""
    return a * b
