from typing import Any


def sum_of_first_n_squares(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{n} is not an integer: {type(n)}")

    if n == 0:
        return 0

    return n**2 + sum_of_first_n_squares(n - 1)


def create_list_comprehension(some_int: int) -> list[Any]:
    return [x**2 for x in range(some_int)]


def create_list_for_loop(some_int: int) -> list[Any]:
    output = []

    for x in range(some_int):
        output.append(x**2)

    return output
