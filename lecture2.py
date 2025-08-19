from typing import Any


def listends_n_items(a: list[Any], n_items: int = 1):  # -> technically tuple
    """Prints the first n and last n items from any inputted list"""
    print(f"First {n_items}: {a[:n_items]}")
    print(f"Last {n_items}: {a[-n_items:]}")


def listends_nothing(a: list[Any]):  # -> technically tuple)
    return a[0], a[-1]


def listends_list(a: list[Any]) -> list[Any]:
    return [a[0], a[-1]]


def listends_tuple(a: list[Any]) -> tuple[Any]:
    return (a[0], a[-1])


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    a, b = listends_nothing(lst)
    print(f"a={a}, b={b}")
    a, b = listends_list(lst)
    print(f"a={a}, b={b}")
    a, b = listends_tuple(lst)
    print(f"a={a}, b={b}")

    lst = "Hello!"
    a, b = listends_nothing(lst)
    print(f"a={a}, b={b}")
    a, b = listends_list(lst)
    print(f"a={a}, b={b}")
    a, b = listends_tuple(lst)
    print(f"a={a}, b={b}")

    listends_n_items(lst, 100)
