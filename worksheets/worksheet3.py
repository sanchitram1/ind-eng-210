# Problem 1
# Write a function called ’mean1’ that takes a list as an input and returns the
# mean of the entries of that list. Add a docstring to this function that explains
# what it does, and veryfy that you can run ’help(mean1)’ in the VSCode interactive
# window or your code after defining it.
def mean1(numbers: list[int | float]) -> float:
    """
    This function returns the mean of a list of numbers.

    Inputs:
      - A list of integers or floats

    Returns:
      - A float that is the mean of the inputted list

    Raises:
      - If it is given a list of anything except ints or floats, it will error"""
    # Guard
    assert all(
        [isinstance(i, int) or isinstance(i, float) for i in numbers]
    ), f"Input contained non-numeric entries: {numbers}"

    # Logic
    current_sum = 0
    total_elements = len(numbers)

    for n in numbers:
        current_sum += n

    return current_sum / total_elements


# Problem 2
def mean2(numbers: list[int | float]) -> float:
    """Write a function called ’mean2’ that enhances ’mean1’ in two ways: First, it as-
    serts that a list is passed in, raising an error otherwise, and second if some item
    of the list is not an int or float, that list item is simply skipped (so you could run
    mean2([2,6,’hi’,7.3]), for example)."""
    # Guard
    assert isinstance(numbers, list)

    # We can just filter the list to include only ints & floats, and pass that on
    # to mean1.
    actual_numbers = [
        item for item in numbers if isinstance(item, int) or isinstance(item, float)
    ]

    return mean1(actual_numbers)


# Problem 3
def myMaxMin(numbers: list[int | float], ignore_negative=False) -> tuple[int | float]:
    """
    Write a function called myMaxMin that returns both the maximum and the minimum
    entry of a list of numbers. Then, modify it to allow us to optionally add a third
    (boolean) parameter that is false by default, but makes the function return 0 in place
    of the max or min if they are negative if the parameter is specified to be True. Test
    that you can call the function with passing 2 or 3 parameters
    """
    # Establish starting point
    current_max = numbers[0]
    current_min = numbers[0]

    # Loop
    for item in numbers[1:]:
        if item > current_max:
            current_max = item

        if item < current_min:
            current_min = item

    if ignore_negative:
        if current_min < 0:
            current_min = 0

        if current_max < 0:
            current_max = 0

    return current_max, current_min


def i_times_sin_i(i: int):
    """Define a function taking integers as inputs and returning the sum i * sin(i)"""
    import numpy as np

    if i == 1:
        return 1 * np.sin(1)

    return i * np.sin(i) + i_times_sin_i(i - 1)


if __name__ == "__main__":
    # Problem 1 tests
    assert mean1([1, 2, 3]) == 2
    assert round(mean1([1.1, 2.2, 3.3]), 2) == 2.2

    try:
        mean1(["Hello", "World"])
    except AssertionError:
        pass

    # Problem 2 tests
    assert mean2([1, "hi", 3]) == 2
    assert round(mean2([2, 6, "hi", 7.3]), 2) == 5.10

    # Problem 3 tests
    assert myMaxMin([1, 2, 3]) == (3, 1)
    assert myMaxMin([-1, -2, -3], True) == (0, 0)
    assert myMaxMin([-1, -2, -3]) == (-1, -3)
    assert myMaxMin([-100, 0, 1], True) == (1, 0)

    # Problem 4
    inputs = range(1, 100, 1)
    vals = [i_times_sin_i(i) for i in inputs]
    max_val, min_val = myMaxMin(vals)

    print(f"Maximum input value: {inputs[vals.index(max_val)]}")
