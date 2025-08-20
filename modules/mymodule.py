def sum_of_first_n_squares(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{n} is not an integer: {type(n)}")

    if n == 0:
        return 0

    return n**2 + sum_of_first_n_squares(n - 1)
