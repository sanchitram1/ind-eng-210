import timeit

import numpy as np

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


def problem2():
    """Initialize a 10x10 Numpy array using np.zeros or np.empty. Then, modify it so
    that each index i row is [i, i+1, ..., i +9]. Next, separately print each column of
    the resulting array."""
    square = 10
    A = np.zeros((square, square))
    pretty_print_array(A, "Original Array")

    for row in range(square):
        for col in range(square):
            A[row, col] = row + col

    pretty_print_array(A, "Modified Array")

    for i in range(square):
        print(f"Column {i+1}")
        print(A[:, i])


def problem3():
    """Assign (not necessarily in one line) variable an array taking values sin(0), sin(0.001),
    sin(0.002), ..., sin(3.999), sin(4). Compare the runtime of finding the max entry of this
    array using a for loop versus using the np.max function; print what relative fraction of
    time it took"""
    A = [np.sin(i / 1000) for i in range(0, 4000, 1)]

    t1 = timeit.timeit(lambda: np.max(A), number=1000)
    print(f"Numpy Max Approach: {t1:.6f} seconds, max_value={np.max(A)}")

    def for_loop_approach(a) -> float:
        # Start
        current_max = a[0]

        # Loop
        for item in a[1:]:
            if item > current_max:
                current_max = item

        return current_max

    t2 = timeit.timeit(lambda: for_loop_approach(A), number=1000)
    print(f"For loop approach: {t2:.6f} seconds, max_value={for_loop_approach(A)}")


if __name__ == "__main__":
    problems = [problem1, problem2, problem3]
    for i, problem in enumerate(problems):
        print()
        print(f"{SEP} PROBLEM {i+1} {SEP}")
        problem()
