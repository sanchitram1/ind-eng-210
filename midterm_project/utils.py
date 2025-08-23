def sep(msg: str, i: int = 50) -> None:
    print(f"{'-' * i + msg + '-' * i}")


def small_sep(msg: str) -> None:
    sep(msg, 20)
