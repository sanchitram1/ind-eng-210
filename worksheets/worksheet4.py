import sys
from math import sin

import numpy as np

from modules.mymodule import time_report

sys.setrecursionlimit(10000000)

SEP = "-" * 10


def pretty_print_array(a, msg: str) -> None:
    print(f"{msg}:\n{a}")


def problem1():
    """Initialize a 6x6 array of ones. Print the the right ”half” (3rd column onwards), and the
    bottom half (3rd row onwards). Next, set the entries of those to be zeros, without using for
    loops, and print the entire modified array to check it worked (so only the top-left quadrant
    will have ones)."""
    A = np.ones((6, 6))

    # Print the right half
    pretty_print_array(A[:, 3:], "Right half")

    # Print the bottom half
    pretty_print_array(A[3:, :], "Bottom half")

    A[:, 3:] = 0
    A[3:, :] = 0
    pretty_print_array(A, "Modified")


def problem2(square: int = 10):
    """Initialize a 10x10 Numpy array using np.zeros or np.empty. Then, modify it so
    that each index i row is [i, i+1, ..., i +9]. Next, separately print each column of
    the resulting array."""
    A = np.zeros((square, square))

    for row in range(square):
        for col in range(square):
            A[row, col] = row + col

    pretty_print_array(A, "Modified Array")


def problem2_vectorized_attempt(dimension: int = 10):
    A = np.zeros((dimension, dimension))

    flat = np.arange(dimension)
    tall = flat.T

    for i in range(dimension):
        A[i, :] += flat
        A[:, i] += tall

    pretty_print_array(A, "Modified Matrix")

    if dimension <= 10:
        for i in range(dimension):
            pretty_print_array(A[:, i], f"Column {i}")


def problem3():
    """Assign (not necessarily in one line) variable an array taking values sin(0),
    sin(0.001), sin(0.002), ..., sin(3.999), sin(4). Find the largest change between two
    consectuive entries in that array"""
    A = np.sin(np.arange(0, 4, 0.001))

    # Create a new array that's basically A, but shifted over
    B = np.append(np.delete(A, 0), np.nan)

    # Grab the absolute difference
    D = abs(A - B)
    print(f"Largest change between two consecutive entries: {np.nanmax(D)}")


def problem4():
    """Do problem 3 without for loops"""
    problem3()


def problem5(some_int: int = 1000000):
    def rec(some_int: int) -> float:
        if some_int == 1:
            return sin(1)

        return (some_int * sin(some_int)) + rec(some_int - 1)

    def numpy_arrays(some_int: int) -> float:
        return np.sum(np.arange(1, some_int, 1) * np.sin(np.arange(1, some_int, 1)))

    def for_loop(some_int: int) -> float:
        return sum([i * sin(i) for i in range(1, some_int, 1)])

    recursion_sum = round(rec(some_int - 1), 6)
    time_report(rec, "Problem 5 (Recursion)", some_int)
    numpy_arrays_sum = round(numpy_arrays(some_int), 6)
    time_report(numpy_arrays, "Problem 5 (Numpy Arrays)", some_int)
    for_loop_sum = round(for_loop(some_int), 6)
    time_report(for_loop, "Problem 5 (For Loop)", some_int)

    # Just make sure they're all doing the same thing
    assert (
        numpy_arrays_sum == for_loop_sum == recursion_sum
    ), f"{numpy_arrays_sum} != {for_loop_sum} != {recursion_sum}"


def do_all_problems():
    problems = [problem1, problem2_vectorized_attempt, problem3, problem4, problem5]
    for i, problem in enumerate(problems):
        print()
        print(f"{SEP} PROBLEM {i+1} {SEP}")
        problem()


if __name__ == "__main__":
    do_all_problems()
    # problem5(1000000)
    # time_report(problem2, "Double For Loop Problem 2", 10000)
    # time_report(problem2_vectorized_attempt, "Vectorized Problem 2", 10000)
    # problem2_vectorized_attempt(10000)
