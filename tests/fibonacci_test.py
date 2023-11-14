import pytest

from src.mylib import fibonacci


# ввод положительных значений
def test_positive_integer_input():

    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]


# ввод отрицательных значений
def test_negative_integer_input():
    assert fibonacci(-1) == "Input should be a positive integer"
    assert fibonacci(-5) == "Input should be a positive integer"


# ввод 0
def test_zero_input():
    assert fibonacci(0) == "Input should be a positive integer"


# ввод больших чисел
def test_large_input():
    a = fibonacci(50)
    assert a[len(a)-1] == 7778742049
    a = fibonacci(100)
    assert a[len(a)-1] == 218922995834555169026


# Run the tests
if __name__ == "__main__":
    pytest.main()
