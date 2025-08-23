import argparse
import sys

import pandas as pd
from matplotlib import pyplot as plt

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

     Source: https://archive.ics.uci.edu/dataset/911/recipe+reviews+and+user+feedback+dataset
    """)


def problem1():
    """Print summary statistics (such as mean, max, min, percentage of occurrence) of
    two important columns in the data"""
    # we can look at stars (ratings of the recipes) and user_reputation (rating of the
    # user)

    # stars
    # note that stars = 0 corresponds to a missing entry, so let's filter it out
    empty_stars_mask = df["stars"] != 0
    sep("Summary Statistics of stars")
    print(f"Mean of stars: {df.loc[empty_stars_mask, :]['stars'].mean():.4f}")
    print(f"Max of stars: {df.loc[empty_stars_mask, :]['stars'].max()}")
    print(f"Min of stars: {df.loc[empty_stars_mask, :]['stars'].min()}")
    print(
        f"Distribution of stars: {df.loc[empty_stars_mask, :]['stars'].value_counts().sort_values(ascending=False)}"
    )

    # user_reputation
    # note that user_reputation is an internal metreic
    sep("Summary statistics of user_reputation")
    print(f"Mean of rep: {df.loc[empty_stars_mask, :]['user_reputation'].mean():.4f}")
    print(f"Max of rep: {df.loc[empty_stars_mask, :]['user_reputation'].max()}")
    print(f"Min of rep: {df.loc[empty_stars_mask, :]['user_reputation'].min()}")
    print(
        f"Distribution of rep: {df.loc[empty_stars_mask, :]['user_reputation'].value_counts().sort_index(ascending=False)}"
    )

    # reply_count
    # the total replies to that comment
    sep("Summary statistics of reply_count")
    print(f"Mean of rep: {df.loc[empty_stars_mask, :]['reply_count'].mean():.4f}")
    print(f"Max of rep: {df.loc[empty_stars_mask, :]['reply_count'].max()}")
    print(f"Min of rep: {df.loc[empty_stars_mask, :]['reply_count'].min()}")
    print(
        f"Distribution of rep: {df.loc[empty_stars_mask, :]['reply_count'].value_counts().sort_index(ascending=False)}"
    )

    # thumbs_up
    # the number of likes or positive reactions a comment got
    sep("Summary statistics of thumbs_up")
    print(f"Mean of rep: {df.loc[empty_stars_mask, :]['thumbs_up'].mean():.4f}")
    print(f"Max of rep: {df.loc[empty_stars_mask, :]['thumbs_up'].max()}")
    print(f"Min of rep: {df.loc[empty_stars_mask, :]['thumbs_up'].min()}")
    print(
        f"Distribution of rep: {df.loc[empty_stars_mask, :]['thumbs_up'].value_counts().sort_index(ascending=False)}"
    )

    # thumbs_down
    # the number of dislikes a given comment has
    sep("Summary statistics of thumbs_down")
    print(f"Mean of rep: {df.loc[empty_stars_mask, :]['thumbs_down'].mean():.4f}")
    print(f"Max of rep: {df.loc[empty_stars_mask, :]['thumbs_down'].max()}")
    print(f"Min of rep: {df.loc[empty_stars_mask, :]['thumbs_down'].min()}")
    print(
        f"Distribution of rep: {df.loc[empty_stars_mask, :]['thumbs_down'].value_counts().sort_index(ascending=False)}"
    )


def problem2():
    """Make a histogram of some important quantity in the data, a scatterplot showing
    the relationship between two columns where we might expect one, and a pivot table"""

    # histogram => stars, because it is discrete and bound
    # scatter => reply_count and thumbs_up + thumbs_down – total reactions
    # pivot table => so for individuals that have high reputation, what's their "reactions?"
    #  we can make reactions some sort of tier to make it meaningful
    #  or, within reputations that are above 50 (which look high), what are ratings?
    #  the assumption is that they are more likely to have pointed ratings
    def stars_histogram():
        empty_stars_mask = df["stars"] != 0
        plt.hist(df.loc[empty_stars_mask, :]["stars"].sort_index(), bins=5)
        plt.title("Distribution of Stars")
        plt.show()

    def scatter():
        df["reactions"] = df["thumbs_up"] + df["thumbs_down"]
        plt.scatter(df["reply_count"], df["reactions"])
        plt.title("Total Replies vs. Total Reactions (thumbs up + thumbs down)")
        plt.show()

    def pivot_table():
        high_reputation_mask = df["user_reputation"] > 50
        print(
            df.loc[high_reputation_mask, :].pivot_table(
                values="comment_id",
                index="user_reputation",
                columns="stars",
                aggfunc="count",
            )
        )

    stars_histogram()
    # interesting that most are 5 star ratings

    scatter()
    # well, these are integers, so the chart is box-like

    pivot_table()
    # lot of NaNs


def problem3():
    """
    Investigate some summary statistic of a column under meaningful conditions on a
    different column (example: Heart disease prevalence in patients with higher than
    average cholesterol, win rate of home teams in sports, number of sales made
    on weekends ...) versus when the condition is not met"""
    # let's focus on thumbs up for when ratings == 5, and when ratings != 5
    # the question would be – are users responding to not highly rated recipe reviews

    # let's focus on one recipe
    non_five_star_mask = df["stars"] != 5
    sep("Mean Thumbs Up For 5 Star Recipe Reviews vs. Not 5 star")
    mean_non_five_star = df.loc[non_five_star_mask, :]["thumbs_up"].mean()
    mean_five_star = df.loc[~non_five_star_mask, :]["thumbs_up"].mean()
    print(f"Not 5 star rated: {mean_non_five_star:.4f}")
    print(f"5 star rated: {mean_five_star:.4f}")


def problem4():
    """Problem 3 with another condition"""

    # let's look at the same, but with a specific recipe
    creamy_chili_mask = df["recipe_code"] == 14299
    non_five_star_mask = df["stars"] != 5

    sep("Mean Thumbs Up For 5 Star Recipe Reviews vs. Not 5 star for Creamy Chili")
    mean_non_five_star = df.loc[non_five_star_mask & creamy_chili_mask, :][
        "thumbs_up"
    ].mean()
    mean_five_star = df.loc[~non_five_star_mask & creamy_chili_mask, :][
        "thumbs_up"
    ].mean()
    print(f"Not 5 star rated: {mean_non_five_star:.4f}")
    print(f"5 star rated: {mean_five_star:.4f}")


def worksheet7():
    """Complete the worksheet"""
    problems = [problem1, problem2, problem3, problem4]

    for i, p in enumerate(problems):
        try:
            sep(f"PROBLEM {i + 1}")
            p()
        except Exception as e:
            raise e


def main():
    worksheet7()


if __name__ == "__main__":
    p = argparse.ArgumentParser(prog="Midterm Project")
    p.add_argument(
        "-d",
        "--describe",
        help="Give me the description of the dataset",
        action="store_true",
    )

    args = p.parse_args()

    if args.describe:
        desc()
        sys.exit(0)

    main()
