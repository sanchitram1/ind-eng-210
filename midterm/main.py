import pandas as pd

df = pd.read_csv("data/olympics.csv")


def main():
    print(df.head())
    print(df.isna())

    print("Question 10")
    print(df["Team"].value_counts().sort_values(ascending=False))

    print("Question 11")
    # The mean result time in rows where the stroke is backstroke is (ANSWER) many
    # seconds slower compared to the mean of rows where stroke is freestyle:
    backstroke = df["Stroke"] == "Backstroke"
    freestyle = df["Stroke"] == "Freestyle"

    print(
        f"{df.loc[backstroke, :]["Results"].mean() - df.loc[freestyle, :]["Results"].mean():.4f}"
    )

    hundred_meters = df["dist_m"] == 100
    print(
        f"Variance of hundred meter results: {df.loc[hundred_meters, ["Results"]].var()}"
    )


if __name__ == "__main__":
    main()
