import random
from typing import Any


def listends_n_items(a: list[Any], n_items: int = 1):  # -> technically tuple
    """Prints the first n and last n items from any inputted list"""
    print(f"First {n_items}: {a[:n_items]}")
    print(f"Last {n_items}: {a[-n_items:]}")


def listends_nothing(a: list[Any]):  # -> technically tuple)
    return a[0], a[-1]


def listends_list(a: list[Any]) -> list[Any]:
    return [a[0], a[-1]]


def listends_tuple(a: list[Any]) -> tuple[Any]:
    return (a[0], a[-1])


def recursive_worksheet2_problem2(n: int) -> int:
    """
    W_0 = 2
    W_n = W_(n-1) ^ W_(n-1)
    """
    if n == 0:
        return 2
    return recursive_worksheet2_problem2(n - 1) ** recursive_worksheet2_problem2(n - 1)


def is_odd(A: int | list[int]) -> bool:
    if isinstance(A, int):
        return A % 2 == 1
    elif isinstance(A, list):
        return [is_odd(a) for a in A]


if __name__ == "__main__":
    print(recursive_worksheet2_problem2(2))
    random_list = [random.randint(1, 100) for _ in range(10)]
    odds = is_odd(random_list)
    print([item for item in zip(random_list, odds)])
