import numpy as np
import pandas as pd


def main():
    df = pd.read_csv("data/premdata_24-25.csv")

    print(df.head())
    home_wins = df["FullTimeResult"] == "H"
    print(f"Home Win Percentage = {np.mean(home_wins)*100:.4f}%")

    away_wins = df["FullTimeResult"] == "A"
    print(f"Away Win Percentage = {np.mean(away_wins)*100:.4f}%")

    a_taylor = df["Ref"] == "A Taylor"
    print(f"Anthony Taylor (scum) refereed {np.mean(a_taylor)*100:.4f}% of games")

    liverpool_home = df["HomeTeam"] == "Liverpool"
    liverpool_away = df["AwayTeam"] == "Liverpool"
    liverpool = liverpool_home | liverpool_away
    print(f"Liverpool played in {np.mean(liverpool)*100:.4f}% of games")

    taylor_liverpool = liverpool & a_taylor
    print(
        f"Anthony Taylor (scum) refereed Liverpool in {np.mean(taylor_liverpool)*100:.4f}% of games"
    )

    df = pd.read_csv("data/yelp.csv")
    print(df.head())

    # fix nan
    is_missing = df == "(Missing)"
    df[is_missing] = np.nan

    outdoor_mask = df["OutdoorSeating"] == "TRUE"
    print(
        f"Mean of ratings using pandas.mean(): {df.loc[outdoor_mask, :]["stars"].mean():.4f}"
    )

    not_outdoor_mask = df["OutdoorSeating"] == "FALSE"
    print(
        f"Mean of ratings for not-outdoors: {df.loc[not_outdoor_mask, :]["stars"].mean():.4f}"
    )

    allow_dogs = df["DogsAllowed"] == "TRUE"
    allow_dogs_indoors = allow_dogs & not_outdoor_mask
    print(
        f"Mean of ratings for allow dogs not outdoor: {df.loc[allow_dogs_indoors, :]["stars"].mean():.4f}"
    )


if __name__ == "__main__":
    main()
