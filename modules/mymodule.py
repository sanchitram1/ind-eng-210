from time import time
from typing import Any, Callable

import numpy as np


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


def create_list_numpy(some_int: int):
    a = np.arange(some_int)
    return a**2


def create_simple_list_for_loop(some_int: int) -> list[int]:
    output = []

    for x in range(some_int):
        output.append(x)

    return output


def create_numpy_array(some_int: int):
    output = np.zeros(some_int, np.int32)

    for x in range(some_int):
        output[x] = x

    return output


def create_numpy_range(some_int: int):
    return np.arange(some_int, dtype=np.int32)


def time_report(function: Callable, msg: str, *args):
    start = time()
    function(*args)
    print(f"{msg}: {time() - start:.6f}")


def sep(msg: str, i: int = 20) -> None:
    print(f"{'-'*i}{msg}{'-'*i}")


def small_sep(msg: str, i: int = 10) -> None:
    sep(msg, i)
