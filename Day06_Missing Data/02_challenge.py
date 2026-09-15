import pandas as pd
import numpy as np


# ------------------------------------------------------------
# Create employee dataset
# ------------------------------------------------------------

df = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": [
        "Amit", "Priya", "Rahul", "Neha",
        "Arjun", "Sneha", "Vikram", "Pooja"
    ],
    "Salary": [
        50000, 55000, np.nan, 60000,
        250000, np.nan, 65000, 70000
    ],
    "Department": [
        "IT", "HR", np.nan, "IT",
        "Finance", "IT", np.nan, "IT"
    ],
    "JoiningDate": [
        "2020-01-10",
        "2020-02-15",
        np.nan,
        "2020-04-20",
        "2020-05-10",
        np.nan,
        "2020-07-15",
        np.nan
    ]
})


print("Original DataFrame:")
print(df)


# ------------------------------------------------------------
# Convert JoiningDate to datetime
# ------------------------------------------------------------

df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])


# ------------------------------------------------------------
# 1. Salary - Median Imputation
# ------------------------------------------------------------

# Median is appropriate for Salary because salary is numeric
# and the dataset contains an outlier (250000).
# The median is less affected by extreme values than the mean.

df["Salary"] = df["Salary"].fillna(df["Salary"].median())


# ------------------------------------------------------------
# 2. Department - Mode Imputation
# ------------------------------------------------------------

# Mode is appropriate for a categorical column because it
# represents the most frequently occurring department.
# Here, "IT" is the most common department.

df["Department"] = df["Department"].fillna(df["Department"].mode()[0])


# ------------------------------------------------------------
# 3. JoiningDate - Forward Fill
# ------------------------------------------------------------

# Forward fill is appropriate because JoiningDate is sequential
# according to EmployeeID. A missing date is filled using the
# most recent known joining date.

df["JoiningDate"] = df["JoiningDate"].ffill()


# ------------------------------------------------------------
# Final cleaned DataFrame
# ------------------------------------------------------------

print("\nCleaned DataFrame:")
print(df)


# ------------------------------------------------------------
# Check for remaining missing values
# ------------------------------------------------------------

print("\nMissing values after cleaning:")
print(df.isna().sum())