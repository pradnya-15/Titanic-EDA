# Project 01: Exploratory Data Analysis (EDA) on Titanic Dataset

## Aim
To perform Exploratory Data Analysis (EDA) on the Titanic dataset using Python and Pandas to identify important passenger survival patterns.

## Objective
- Load and explore the Titanic dataset.
- Perform DataFrame operations using Pandas.
- Identify and handle missing values.
- Check and remove duplicate records.
- Analyze survival rates based on gender, passenger class, and age group.
- Generate meaningful statistical insights.

## Tools Used
- Python 3.10+
- VS Code
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset
Titanic dataset loaded using the Seaborn library.

```python
df = sns.load_dataset("titanic")
```

## Procedure
1. Import the required Python libraries.
2. Load the Titanic dataset.
3. Display the first five rows using `head()`.
4. Examine the dataset using `info()` and `describe()`.
5. Identify missing values using `isnull().sum()`.
6. Handle missing values using median and mode.
7. Remove the deck column because it contains many missing values.
8. Identify and remove exact duplicate records.
9. Perform grouping and aggregation using `groupby()`.
10. Analyze survival rates by gender, passenger class, and age group.
11. Calculate overall survival statistics.
12. Save the cleaned dataset as a CSV file.

## Analysis Questions
1. Did women survive more often than men?
2. Did passenger ticket class affect survival?
3. Was age related to survival?

## Output
The program displays:
- Dataset information and statistical summary.
- Missing values before and after cleaning.
- Duplicate record count.
- Survival rate by gender.
- Survival rate by passenger class.
- Survival rate by age group.
- Overall survival statistics.

## Result
Exploratory Data Analysis was successfully performed on the Titanic dataset using Pandas. Missing values and duplicate records were handled, and passenger survival patterns were analyzed using grouping and aggregation techniques.
