import argparse

import numpy as np

from modules.mymodule import time_report
from worksheets.worksheet3 import mean1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Main function for IND ENG 210",
        description="Provides an interface for all the things I write for IND ENG 210",
    )

    parser.add_argument("-n", "--number", type=int)

    args = parser.parse_args()

    number = args.number

    A = np.arange(number)

    time_report(mean1, "Mean 1 Runtime", A)
    time_report(np.mean, "np.mean Runtime", A)
