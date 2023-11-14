import pytest
from mylib import bubble_sort


# для списка с int
def test_integer_list():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([5, 8, 2, 9, 3]) == [2, 3, 5, 8, 9]


# для списка с string
def test_string_list():
    assert bubble_sort(['c', 'b', 'a']) == ['a', 'b', 'c']
    assert bubble_sort(['zebra', 'lion', 'elephant']) == ['elephant', 'lion', 'zebra']


# для пустого списка
def test_empty_list():
    assert bubble_sort([]) == []


# для списка с одним элементом
def test_single_element_list():
    assert bubble_sort([5]) == [5]


# для списка с повторяющимися элементами
def test_duplicate_elements_list():
    assert bubble_sort([3, 2, 3, 1, 2]) == [1, 2, 2, 3, 3]


# некорректный ввод данных в список
def test_non_integer_string_elements():
    with pytest.raises(TypeError):
        bubble_sort([1, 'a', 3])


if __name__ == "__main__":
    pytest.main()
