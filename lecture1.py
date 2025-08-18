# Lecture 1: Intro to Python.


def worksheet1():
    # Worksheet 1

    # Formatting stuff
    skip = True
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
    lst2 = [lst1, "list2"]

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

        try:
            for i in range(1000):
                for j in range(1000):
                    if i**2 + j**2 == 223065:
                        print(f"Problem 1: {i}^2 + {j}^2 ?= 223065")
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

        output = []
        for i in range(n):
            output.append(i**2)

        print(f"Problem 3: The list is {output}")

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
        raise NotImplementedError("Problem 5 not started")

    def problem6():
        raise NotImplementedError("Problem 6 not started")

    problems = [problem1, problem2, problem3, problem4, problem5, problem6]
    for problem in problems:
        try:
            problem()
            print("-" * 10)
        except NotImplementedError as e:
            print(e)


if __name__ == "__main__":
    worksheet2()
