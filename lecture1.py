# Lecture 1: Intro to Python.
from collections import defaultdict

import numpy as np


def worksheet1():
    # Worksheet 1

    # Formatting stuff
    SEP = "-" * 10
    BIG_SEP = "-" * 20

    # Problem 1
    name = "Sanchit Ram Arvind"
    age = 29
    height = 67  # inches
    print(f"{BIG_SEP} PROBLEM 1 {BIG_SEP}")
    print(f"{SEP} (i) {SEP}")
    print(
        "Hi! My name is",
        name,
        "\nI am",
        age,
        "years old, and am",
        height,
        "inches tall",
    )
    print(f"{SEP} (ii) {SEP}")
    print(
        f"Hi! My name is {name}\nI am {age} years old, and am {height:.1f} inches tall"
    )

    # Problem 2
    print()
    print(f"{BIG_SEP} PROBLEM 2 {BIG_SEP}")
    year = input("Tell me the year: ").strip()
    day = input("Tell me the day: ")
    time = input("Tell me the time: ")
    print("\tYear is", year, "\n\tDay is", day, "\n\tTime is", time)
    print("Year is 2025:", year == "2025")

    # Problem 3
    print()
    print(f"{BIG_SEP} PROBLEM 3 {BIG_SEP}")
    x = 61
    y = 50
    z = 11
    print(f"{x} - {y} == {z}", x - y == z)
    print(f"{x / 10} - {y / 10} == {z / 10}", x / 10 - y / 10 == z / 10)
    print("Probably because...", x / 10 - y / 10, "is not equal to", z / 10)

    # Problem 4
    print()
    # print(f"{BIG_SEP} PROBLEM 4 {BIG_SEP}")
    b = 1
    c = int(input("Enter an integer: "))
    print(f"{c} * 1 == {c}:", b * c == c)
    b /= 10
    print(f"{c} * 1/10 == {c / 10}:", b * c == c / 10)

    # Problem 5
    print()
    print(f"{BIG_SEP} PROBLEM 5 {BIG_SEP}")
    str1 = "String 1"
    str2 = "String 2"
    lst1 = ["list1", "1"]

    print(f"Adding two strings {str1} + {str2}:", str1 + str2)
    # print(f"Subtracting two strings {str1} - {str2}", str1 - str2) # Can't subtract strings
    # print(f"Multiply two strings {str1} * {str2}", str1 * str2) # Can't multiply strings
    # print(f"Multiply two lists {lst1} * {lst2}", lst1 * lst2)  # Can't multiply lists
    print(f"Multiply string by an integer {str1} * 10:", str1 * 10)
    print(f"Multiplying list by an integer {lst1} * 10:", lst1 * 10)
    # print(f"Divide two strings: {str1} / {str2}", str1 / str2)  # Can't divide strings
    # print(f"Divide two lists: {lst1} / {lst2}", lst1 / lst2)  # Can't divide lists


def while_loops():
    some_bool = True
    while some_bool:
        some_bool = False
        print("Hello World")


def worksheet2():
    def problem1():
        """There is a pair of integers x, y such that x^2 + y^2 = 223065.
        Use for or while loops to find them!"""

        class Found(Exception):
            pass

        # try:
        #     for i in range(1000):
        #         for j in range(1000):
        #             if i**2 + j**2 == 223065:
        #                 print(f"Problem 1: {i}^2 + {j}^2 ?= 223065")
        #                 raise Found
        # except Found:
        #     pass

        # The better way to do this is actually to ensure you're hitting every pair
        # of integers sysmetically:

        M = 223065
        N = int(np.sqrt(M))
        try:
            for i in range(N):
                for j in range(i):
                    if i**2 + j**2 == M:
                        print(f"Problem 1: {i}^2 + {j}^2 == 223065:", i**2 + j**2)
                        raise Found
        except Found:
            pass

    def problem2():
        """Define W0 = 2 and Wn = W(n-1)**W(n-1)
        for all integers n ≥ 1. Use a while loop to find the
        smallest n such that Wn > 10**30"""
        start = 0
        val = 2
        while val < 10**30:
            start += 1
            val = val**val
        print(f"Problem 2: Smallest n for our function is {start}")

    def problem3(n: int = 10) -> list[int]:
        """Create a list of length 10 where entry i has value 0^2 + 1^2 + 2^2 + ... + i^2
        (without using the formula for that if you happen to know it). Can you do it
        with only one for loop"""

        # output = []
        # for i in range(n):
        #     output.append(i**2)

        # print(f"Problem 3: The list is {output}")

        # LMAO – I totally misunderstoof this assignment.
        # The point is that the list should have each element as the sum of squares up
        # to that index, not just a list of squares
        N = 10
        output = [0]

        for i in range(1, N):
            output.append(i**2 + output[i - 1])

        print(f"Problem 3: {output}")

    def problem4():
        """Set n = 100 and create two nested for loops iterating i and j through range(n).
        Can you find a way to exit both for loops when i = 49 and j = 76? So after you
        run it, i should have value 49 and j should have value 76."""
        n = 100
        for i in range(n):
            for j in range(n):
                if j == 76:
                    break
            if i == 49:
                break

        print(f"Problem 4: On exiting, i = {i}, j = {j}")

    def problem5():
        """Set A to be a list of numbers of your choice. Set B equal to A.
        Use for loops to set each entry in B equal to itself plus all the
        ’later entries’ (entries corresponding to a larger index) in B. After doing
        that (to B only), what is the value of A?"""
        print("Problem 5:")

        # Get the input
        bad_input = True
        while bad_input:
            ask = input("Enter a comma-separated list of numbers: ")
            try:
                a = [int(i.strip()) for i in ask.split(",")]
                bad_input = False
            except ValueError as e:
                print(f"Couldn't parse input {ask}: {e}")
        print(f"User inputted: {a}")

        # Set b
        b = a

        # Set each entry in `b` equal to itself plus all later entries
        for idx in range(len(b)):
            b[idx] += sum(b[idx + 1 :])

        print(f"Original input: {a}")
        print(f"Sum of later entries: {b}")

    def problem6():
        """
        Initialize an empty dictionary. Ask the user for their name, and then for their
        major, and add it to the dictionary. Suppose that user then leaves and a new
        person comes along.
        Your code for this problem should continue running, asking for users’ name and
        major, which are then added to the dictionary, until a user enters -1 as their
        name or major, upon which the program ends.
        """
        print("Problem 6")
        students = defaultdict(list)
        run = True
        while run:
            name = input("Enter your name: ")

            # Exit condition
            if name == "-1":
                break

            # Ask for major
            major = input("Enter your major: ")

            # Create the student
            student = {"name": name.strip(), "major": major.strip()}

            # Add the student to the output
            students["students"].append(student)

        print(f"Students: {students.items()}")

    problems = [problem1, problem2, problem3, problem4, problem5, problem6]
    for problem in problems:
        try:
            problem()
            print("-" * 10)
        except NotImplementedError as e:
            print(e)


def nested_for_loop_exit():
    import random
    import timeit

    N = 10000
    exit_i = random.randint(0, N)
    exit_j = random.randint(0, N)

    print(f"Exit conditions: i={exit_i}, j={exit_j}")

    def double_if_double_break(n: int = N):
        for i in range(n):
            for j in range(n):
                # Break 1
                if j == exit_j:
                    break
            # Break 2
            if i == exit_i:
                break

    t1 = timeit.timeit(double_if_double_break, number=10)
    print(f"Approach 1: {t1:.6f} seconds")

    def exit_loop_condition(n: int = N):
        exit_loop = False
        for i in range(n):
            for j in range(n):
                exit_loop = i == exit_j and j == exit_j
                if exit_loop:
                    break

            if exit_loop:
                break

    t2 = timeit.timeit(exit_loop_condition, number=10)
    print(f"Approach 2: {t2:.6f} seconds")


if __name__ == "__main__":
    # worksheet2()
    nested_for_loop_exit()
