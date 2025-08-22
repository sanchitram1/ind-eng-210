import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data/alzheimers.csv")

if __name__ == "__main__":
    print(df.head())
    print()

    print(f"Unique ages: {df["Age"].unique()}")
    print(f"Average age: {df["Age"].mean()}")

    total_rows = len(df)
    family_history = df["FamilyHistoryAlzheimers"].sum()
    print(f"% of people with family history = {(family_history / total_rows)*100:.2f}%")

    plt.hist(df["Age"])
    plt.title(f"Age Distribution (Average Age = {df["Age"].mean():.0f})")
    plt.show()
