from collections import defaultdict

import numpy as np


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

        # LMAO – I totally misunderstood this assignment.
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
