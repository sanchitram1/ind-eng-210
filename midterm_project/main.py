import argparse
import sys

import pandas as pd

from utils import sep

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
    # we can look at stars (ratings of the recipes) and reputation_score (rating of the
    # user)

    # stars
    # note that stars = 0 corresponds to a missing entry, so let's filter it out
    empty_stars_mask = df["stars"] != 0
    sep("Summary Statistics of stars")
    print(f"Mean of stars: {df.loc[empty_stars_mask, :]['stars'].mean():.4f}")
    print(f"Max of stars: {df.loc[empty_stars_mask, :]['stars'].max()}")
    print(f"Min of stars: {df.loc[empty_stars_mask, :]['stars'].min()}")
    print(
        f"Distribution of stars: {df.loc[empty_stars_mask, :]['stars'].value_counts()}"
    )

    # reputation_score
    # note that reputation_score is an internal metreic
    sep("Summary statistics of reputation_score")
    #
    # plt.hist(df.loc[empty_stars_mask, :]["stars"])
    # plt.title("Stars Distribution")
    # plt.show()


def main():
    worksheet7()


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
