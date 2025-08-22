"""
Write code that does the following:
10,000 times,generate a random list of 25 people's birthdays
(i.e. random integers from 1 to 365)
and check whether any two or more birthdays in the generated list are the same.
Print out what percentage of those lists contained a shared birthday.
"""

from numpy import array, unique
from numpy.random import random_integers


def main():
    repetitions = 10000
    people = 25
    shared = 0

    for cycle in range(repetitions):
        birthdays = array([random_integers(1, 365) for _ in range(people)])
        unique_birthdays = unique(birthdays)

        if len(birthdays) != len(unique_birthdays):
            print(f"Cycle {cycle+1} had a shared birthday")
            shared += 1

    print(f"{(shared / repetitions) * 100:.2f}% of cycles had shared birthdays")


if __name__ == "__main__":
    main()
