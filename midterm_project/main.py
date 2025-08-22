import argparse
import sys

import pandas as pd

df = pd.read_csv("data/recipes.csv", index_col=0)


def desc():
    print("""
    This is a dataset about reviews and comments of recipes hosted on some culinary
    website domain. Some key definitions include:

     - `best_score`: score of the comment, likely used by the site the help determine 
     the order the comments appear in	 
     - `stars`: the ratings the commenting user gave to the recipe
     - `reply_count:` replies to that specific comment
     - `user_reputation:` some sort of reputation index for the user
    """)


def worksheet7():
    """
    - Print summary statistics (such as mean, max, min, percentage of occurrence) of
      two important columns in the data
    - Make a histogram of some important quantity in the data, a scatterplot showing
      the relationship between two columns where we might expect one, and a pivot table
    - Investigate some summary statistic of a column under meaningful conditions on a
      different column (example: Heart disease prevalence in patients with higher than
      average cholesterol, win rate of home teams in sports, number of sales made
      on weekends ...) versus when the condition is not met
    - The previous bullet point but with two or more conditions
    """
    # we can look at stars and


def main():
    print(f"Columns: {df.columns}")
    print(f"DF Shape: {df.shape}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(prog="Midterm Project")
    p.add_argument(
        "-d",
        "--describe",
        help="Give me the description of complex fields",
        action="store_true",
    )

    args = p.parse_args()

    if args.describe:
        desc()
        sys.exit(0)

    main()
