import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS - TITANIC DATASET")
print("=" * 60)

df = sns.load_dataset("titanic")

print("\n1. DATASET SHAPE")
print(df.shape)

print("\n2. FIRST FIVE ROWS")
print(df.head())

print("\n3. DATASET INFORMATION")
df.info()

print("\n4. STATISTICAL DESCRIPTION")
print(df.describe())

print("\n5. MISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

df["age"] = df["age"].fillna(
    df.groupby(["pclass", "sex"])["age"].transform("median")
)

df["embarked"] = df["embarked"].fillna(
    df["embarked"].mode()[0]
)

df = df.drop(columns=["deck"])

print("\n6. MISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

duplicate_count = df.duplicated().sum()

print("\n7. DUPLICATE ROWS")
print("Number of duplicate rows:", duplicate_count)

df = df.drop_duplicates()

print("Duplicates after cleaning:", df.duplicated().sum())

print("\n8. DATA TYPES")
print(df.dtypes)

print("\n9. SURVIVAL RATE BY GENDER")

gender_survival = df.groupby("sex", observed=True)["survived"].mean()

print((gender_survival * 100).round(2))

print("\n10. SURVIVAL RATE BY PASSENGER CLASS")

class_survival = df.groupby("pclass", observed=True)["survived"].agg(
    ["mean", "count"]
)

class_survival["mean"] = class_survival["mean"] * 100

print(class_survival.round(2))

df["age_band"] = pd.cut(
    df["age"],
    bins=[0, 12, 18, 40, 60, 100],
    labels=["Child", "Teen", "Adult", "Middle-aged", "Senior"]
)

print("\n11. SURVIVAL RATE BY AGE GROUP")

age_survival = df.groupby("age_band", observed=True)["survived"].mean()

print((age_survival * 100).round(2))

print("\n12. OVERALL SURVIVAL ANALYSIS")

survived = df["survived"].sum()
not_survived = (df["survived"] == 0).sum()

print("Total passengers:", len(df))
print("Passengers survived:", survived)
print("Passengers not survived:", not_survived)

print("Overall survival rate:",
      round(df["survived"].mean() * 100, 2), "%")

import os

# Save CSV in the same folder as the Python program
folder_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(folder_path, "titanic_cleaned.csv")

df.to_csv(file_path, index=False)

print("\nCSV FILE CREATED SUCCESSFULLY!")
print("File location:", file_path)
print("File exists:", os.path.exists(file_path))
print("\nCleaned dataset saved successfully!")

print("\n" + "=" * 60)
print("EDA ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)
