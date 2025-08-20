import argparse
from time import time

from modules.mymodule import create_list_comprehension, create_list_for_loop

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Main function for IND ENG 210",
        description="Provides an interface for all the things I write for IND ENG 210",
    )

    parser.add_argument("-n", "--number", type=int)

    args = parser.parse_args()

    number = args.number

    start_time = time()
    lst = create_list_comprehension(number)
    print(f"List comprehension time: {time() - start_time}")

    start_time = time()
    lst = create_list_for_loop(number)
    print(f"For loop time: {time() - start_time}")
