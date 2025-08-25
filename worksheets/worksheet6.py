import pandas as pd
from matplotlib import pyplot as plt

from modules.mymodule import sep, small_sep

# Accessible by everything
df = pd.read_csv("data/diabetes.csv")


def problem1():
    """
    To get an idea of the data, check the head of the dataframe and types of the columns.
    Print out the unique values in the outcome column, and the max and min values present
    in Blood Pressure and Insulin.
    """
    small_sep("Head of df")
    print(df.head())
    small_sep("Types of df")
    print(df.dtypes)
    small_sep("Unique values of outcome")
    print(df["Outcome"].unique())
    small_sep(
        f"Blood pressure: max={df["BloodPressure"].max()}, min={df["BloodPressure"].min()}"
    )
    small_sep(f"Insulin: max={df["Insulin"].max()}, min={df["Insulin"].min()}")


def problem2():
    """
    Make a scatterplot of Glucose versus Insulin levels. Next, make a scatterplot of Glucose
    versus Insulin levels only using rows of the data where neither value is 0.
    """
    print("See graph")
    x = df["Glucose"]
    y = df["Insulin"]
    plt.scatter(x, y, c="blue", s=1, label="Including 0s")

    mask = (df["Glucose"] != 0) & (df["Insulin"] != 0)
    plt.scatter(
        df.loc[mask, ["Glucose"]],
        df.loc[mask, ["Insulin"]],
        c="red",
        s=1,
        label="Excluding 0s",
    )

    # Chart config
    plt.title("Glucose vs. Insulin")
    plt.legend()
    plt.show()


def problem3():
    """
    Modify the Pregnancies table to only have 0 or 1 depending on whether the patient has
    had 0 or more than 0 pregnancies. Then a pivot table with pregnancies and outcome as
    the index and columns, and glucose as the value.
    """
    small_sep("Preprocessed pregnancies")
    print(f"Unique: {df["Pregnancies"].unique()}")
    print(f"Counts: {df["Pregnancies"].value_counts()}")

    # Using masks
    mask = df["Pregnancies"] > 0
    df.loc[mask, ["Pregnancies"]] = 1

    small_sep("Post processed pregnancies")
    print(f"Unique: {df["Pregnancies"].unique()}")
    print(f"Counts: {df["Pregnancies"].value_counts()}")

    print(pd.pivot_table(df, values="Glucose", index="Pregnancies", columns="Outcome"))


def problem4():
    """
    Within rows with a nonzero entry for skin thickness: Find the mean of skin thickness, and
    print out the ’outcome’ percentage of patients with skin thickness above versus below the
    mean.
    """
    mask = df["SkinThickness"] != 0
    mean_thickness = df.loc[mask, :]["SkinThickness"].mean()
    print(f"Mean Skin Thickness for nonzero skin thickness(i?): {mean_thickness:.2f}")

    above_mean_thickness = df["SkinThickness"] > mean_thickness
    outcome_above_mean_thickness = df.loc[above_mean_thickness, :]["Outcome"].mean()
    outcome_below_mean_thicness = 1 - outcome_above_mean_thickness
    msg = "Outcome Percentage for patients with skin thickness above vs. below mean ="
    print(
        f"{msg} {outcome_above_mean_thickness*100:.2f}% vs. {outcome_below_mean_thicness*100:.2f}%"
    )


def problem5():
    """
    Let’s make a new column ’BP Risk’, which is 0 if Bloodpressure is below 90, 1 if it
    is below 100, 2 if it is below 110, and 3 otherwise. Make a box plot of BMI with
    your new BP Risk column as the index.
    (and of course I mean make BP risk 1 if BP is below 100 and above 90, and so on)
    """
    mask_below_90 = df["BloodPressure"] < 90
    mask_below_100 = (df["BloodPressure"] < 100) & (df["BloodPressure"] >= 90)
    mask_below_110 = (df["BloodPressure"] < 110) & (df["BloodPressure"] >= 100)

    # Assign column
    df.loc[mask_below_90, ["BP Risk"]] = 0
    df.loc[mask_below_100, ["BP Risk"]] = 1
    df.loc[mask_below_110, ["BP Risk"]] = 2
    df.loc[df["BP Risk"].isna(), ["BP Risk"]] = 3


def main():
    do_worksheet()


def do_worksheet():
    problems = [problem1, problem2, problem3, problem4, problem5]
    for i, p in enumerate(problems):
        sep(f"PROBLEM {i+1}")

        try:
            p()
        except NotImplementedError:
            print(f"⏳ Problem {i+1} not started")
        except Exception as e:
            raise e

        print()


if __name__ == "__main__":
    main()
