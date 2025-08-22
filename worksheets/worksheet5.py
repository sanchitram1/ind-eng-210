from random import random

import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_equal

from modules.mymodule import sep, small_sep
from worksheets.worksheet4 import pretty_print_array


def problem1():
    """
    Problem:

        Plot a graph for f (x) = x − sin(x) from 0 to 8. Use a spacing of 0.01 for your
        x points in creating the graph. Next, use an index mask to select x coordinates
        where f(x) > x, and call the set of those coordinates Z. Then make a scatter
        plot of (Z, f(Z)) over your original plot using plt.scatter
        (where plt is from import matplotlib.pyplot as plt).
    """
    x = np.arange(0, 8, 0.01)
    y = x - np.sin(x)
    plt.title("Problem 1")
    plt.plot(x, y)

    # Mask
    z_x = x[x <= y]
    z_y = y[x <= y]
    plt.scatter(z_x, z_y)

    plt.show()


def problem2():
    """
    Problem:

        Generate a list of 30 random numbers between 0 and 1. Make y a list where the
        nth entry is the mean of the first n generated numbers. Plot the values of y on
        the y axis, with the corresponding indices on the x axis. Next, in the same
        plot, add a line with constant value of 0.5 to visualize what is happening
    """
    size = 30
    x = [random() for _ in range(size)]
    y = [np.mean(x[: i + 1]) for i in range(size)]
    for i, j in zip(x, y):
        print(f"{i:.4f}, {j:.4f}")

    plt.title("Problem 2")
    plt.scatter(np.arange(30), y, s=5)
    plt.hlines(y=0.5, xmin=0, xmax=size)
    plt.ylim(bottom=0, top=1)

    plt.show()


def problem4():
    """
    Problem:

        Download the GPA-SAT data.csv file from bCourses, and import it as a numpy array.
        Answer the following questions (using numpy functions and masking):
            • What are the average SAT scores and GPAs, and what are their standard deviations?
            • Using only the ”lower half” of the table (rows (number of rows / 2) onwards), what
            is the average SAT score and GPA?
            • Make a scatterplot of SAT scores versus GPAs from this dataset.
            • How many students’ SAT scores are above 1900, and what is the average GPA among
            those students? (Use masks!)
            • There is only one student in the dataset with a GPA under 2.6 whose SAT score is
            above 1750. Can you do this with masking? (hint: you can use * on two masks as
            entry-wise ”and”)
    """
    # safe open
    with open("data/GPA-SAT-Data-Fall-2025.csv", "r", encoding="utf-8-sig") as f:
        sat_data = np.genfromtxt(f, delimiter=",")

    # problem a
    small_sep("a")
    print(
        f"SAT Scores\nAverage={np.mean(sat_data[:,0]):.2f}, Std Dev={np.std(sat_data[:,0]):.2f}"
    )
    print(
        f"GPAs\nAverage={np.mean(sat_data[:,1]):.2f}, Std Dev={np.std(sat_data[:,1]):.2f}"
    )

    # problem b
    lower_half = sat_data[int(sat_data.shape[0] / 2) :, :]
    small_sep("b")
    print(
        f"Lower Half\nAvg SAT Score={np.mean(lower_half[:, 0]):.2f}, Avg GPA={np.mean(lower_half[:, 1]):.2f}"
    )

    # problem c
    plt.title("Scatter Plot of SAT Scores vs. GPA")
    plt.scatter(sat_data[:, 0], sat_data[:, 1])
    plt.show()

    # problem d
    small_sep("d")
    above_1900 = sat_data[sat_data[:, 0] > 1900, :]
    print(
        f"Average GPA for students with above 1900 on SAT={np.mean(above_1900[:, 1]):.2f}"
    )

    # problem e
    small_sep("e")
    special_student = sat_data[(sat_data[:, 1] < 2.6) * (sat_data[:, 0] > 1750)]
    special_student_and = sat_data[(sat_data[:, 1] < 2.6) & (sat_data[:, 0] > 1750)]

    assert_equal(special_student, special_student_and)
    assert special_student.shape[0] == 1, f"Found {special_student.shape} students"
    print(f"Special student scores={special_student}")


def problem3():
    """
    Problem:

        Download the temperatures.csv data from bCourses, import it as a numpy array, and
        answer the following:
            • An invalid reading is any temperature below 0 or above 100 degrees Celsius. Create
            and print a mask that identifies all invalid readings; then also print all of the invalid
            readings themselves.
            • Use the mask from the previous step to create a new array called valid temps that
            contain only the valid readings. Print the mean, min, max, and standard deviation
            of these valid temperature readings.
            • Instead of just removing the invalid values, let’s replace each invalid value by the
            average of the values immediately before and after it, as our ”best estimate” of those
            temperatures. (What would you do if the first or last value was invalid?)
            • Using valid temps, create a mask to find how many days the temperature was above
            24.0 degrees. Print the final count (not the array) of how many of these hot days
            there were
    """
    temperatures = np.genfromtxt("data/temperatures.csv")

    small_sep("a")
    invalid = temperatures[(temperatures < 0) | (temperatures > 100)]
    print(f"Invalid readings: {invalid}")

    small_sep("b")
    valid = temperatures[np.logical_not((temperatures < 0) | (temperatures > 100))]
    print(f"Valid readings: {valid}")

    small_sep("c")
    new_temps = temperatures.copy()
    is_invalid = (new_temps < -50) | (new_temps > 100)

    for i in range(1, len(new_temps) - 1):
        if is_invalid[i]:
            new_temps[i] = (new_temps[i - 1] + new_temps[i + 1]) / 2

    print(f"Corrected temperatures: {new_temps}")

    small_sep("d")
    hot_days = np.sum(new_temps > 24)
    print(f"Number of hot days: {hot_days}")


def do_worksheet():
    problems = [problem1, problem2, problem3, problem4]
    for i, p in enumerate(problems):
        sep(f"PROBLEM {i+1}")

        try:
            p()
        except NotImplementedError:
            print(f"⏳ Problem {i+1} not started")
        except Exception as e:
            raise e

        print()


def assets_assignment():
    """
    Columns are:
        "goldprice_change",
        "copperprice_change",
        "SP500price_change",
        "oilprice_change",
        "NASDAQprice_change",
        "steelprice_change",
    """
    data = np.genfromtxt("data/assets.csv", delimiter=",", skip_header=True)
    print(data.shape, id(data))

    gold_price_up = data[data[:, 0] > 0]
    print(gold_price_up.shape, id(gold_price_up))

    gold_and_copper_price_up = data[(data[:, 0] > 0) & (data[:, 1] > 0)]
    print(gold_and_copper_price_up.shape, id(gold_and_copper_price_up))

    print()
    try:
        gold_and_copper_price_up = data[data[:, 0] > 0 & data[:, 1] > 0]
        print("Whoops, this succeeded")
    except TypeError as e:
        print(f"Multiple index masks need parentheses to be chained: {e}")

    print()
    try:
        gold_and_copper_price_up = data[(data[:, 0] > 0) and (data[:, 1] > 0)]
        print("Whoops, this succeeded")
    except ValueError as e:
        print(f"`and` is just not implemented: {e}")


def concatenate_exercise():
    N = 10
    A = np.ones((1, N))
    B = np.ones((1, N)) + 5
    pretty_print_array(A, "A")
    pretty_print_array(B, "B")
    pretty_print_array(np.concatenate((A, B), axis=0), "A+B, axis=0")
    pretty_print_array(np.concatenate((A, B), axis=1), "A+B, axis=1")


if __name__ == "__main__":
    do_worksheet()
    # assets_assignment()
    # problem3()
    # concatenate_exercise()
