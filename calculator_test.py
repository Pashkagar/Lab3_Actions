import pytest
from mylib import calculator


# проверка +
def test_addition():
    assert calculator(3, 5, "+") == 8
    assert calculator(-2, 2, "+") == 0


# проверка -
def test_subtraction():
    assert calculator(5, 3, "-") == 2
    assert calculator(2, 5, "-") == -3


# проверка *
def test_multiplication():
    assert calculator(3, 4, "*") == 12
    assert calculator(-2, 5, "*") == -10


# проверка /
def test_division():
    assert calculator(8, 4, "/") == 2
    assert calculator(7, 2, "/") == 3.5


# проверка деления на 0
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator(5, 0, "/")


# некорректный ввод
def test_non_numeric_input():
    with pytest.raises(TypeError):
        calculator("abc", 3, "+")


if __name__ == "__main__":
    pytest.main()

