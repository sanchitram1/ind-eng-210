from typing import Any


def homework1(some_list: list[Any]) -> list:
    """Given some list `A`, this function reverses it and checks if it is a palindrome"""

    reversed = []
    for i in range(len(some_list)):
        reversed.append(some_list[len(some_list) - 1 - i])

    if some_list == reversed:
        print(f"A ({some_list}) is a palindrome")

    return reversed


def test_non_palindrome():
    lst = [1, 2, 3]
    assert homework1(lst) == [3, 2, 1], "Assertion 1 failed"

    lst = ["A", "p", "p", 2]
    assert homework1(lst) == [2, "p", "p", "A"], "Assertion 2 failed"

    lst = "Hello"
    assert homework1(lst) == ["o", "l", "l", "e", "H"], "Assertion 3 failed"


def test_palindrome():
    lst = "radar"
    # Note that this one won't print, but that strings are technically lists
    # is a weird edge case
    assert homework1(lst) == ["r", "a", "d", "a", "r"], "Assertion 4 failed"

    lst = ["r", "a", "d", "a", "r"]
    assert homework1(lst) == ["r", "a", "d", "a", "r"], "Assertion 5 failed"

    lst = [1, 0, 1]
    assert homework1(lst) == [1, 0, 1], "Assertion 6 failed"


if __name__ == "__main__":
    test_non_palindrome()
    test_palindrome()
