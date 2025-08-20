import argparse

from modules.mymodule import sum_of_first_n_squares

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Main function for IND ENG 210",
        description="Provides an interface for all the things I write for IND ENG 210",
    )

    parser.add_argument("-n", "--number", type=int)

    args = parser.parse_args()

    number = args.number

    print(sum_of_first_n_squares(number))
