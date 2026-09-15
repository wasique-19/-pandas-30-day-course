import pandas as pd
import numpy as np


# ============================================================
# 1. Create a DataFrame with missing values
#    and count missing values using isna().sum()
# ============================================================

df1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, np.nan, 22, np.nan],
    "City": ["Delhi", "Mumbai", np.nan, "Pune"]
})

print("1. Original DataFrame:")
print(df1)

print("\nMissing values in each column:")
print(df1.isna().sum())


# ============================================================
# 2. Drop all rows containing any missing value
# ============================================================

df2 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, np.nan, 22, np.nan],
    "City": ["Delhi", "Mumbai", np.nan, "Pune"]
})

print("\n\n2. DataFrame before dropna():")
print(df2)

df2_clean = df2.dropna()

print("\nDataFrame after dropna():")
print(df2_clean)


# ============================================================
# 3. Fill numeric missing values with mean
#    Fill categorical missing values with "Unknown"
# ============================================================

df3 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, np.nan, 22, 24],
    "City": ["Delhi", np.nan, "Mumbai", np.nan]
})

print("\n\n3. DataFrame before filling:")
print(df3)

# Fill missing Age values with the mean of Age
df3["Age"] = df3["Age"].fillna(df3["Age"].mean())

# Fill missing City values with "Unknown"
df3["City"] = df3["City"].fillna("Unknown")

print("\nDataFrame after filling:")
print(df3)


# ============================================================
# 4. Compare dropna() with subset=["ColA"]
# ============================================================

df4 = pd.DataFrame({
    "ColA": [10, np.nan, 30, 40],
    "ColB": ["A", "B", np.nan, "D"]
})

print("\n\n4. Original DataFrame:")
print(df4)

# Without subset:
# Removes a row if ANY column contains a missing value.
print("\nUsing dropna() without subset:")
print(df4.dropna())

# With subset=["ColA"]:
# Removes a row ONLY when ColA contains a missing value.
# Missing values in other columns, such as ColB, are ignored.
print("\nUsing dropna(subset=['ColA']):")
print(df4.dropna(subset=["ColA"]))


# ============================================================
# 5. Forward fill for time-ordered data
# ============================================================

df5 = pd.DataFrame({
    "Date": pd.date_range("2026-01-01", periods=7),
    "Temperature": [20, 21, np.nan, np.nan, 24, np.nan, 26]
})

print("\n\n5. Original time-ordered DataFrame:")
print(df5)

# Forward fill copies the previous available temperature
# into the missing value.
#
# This makes sense for time-ordered data because a missing
# reading can reasonably be estimated from the most recent
# known reading.
#
# Forward fill may NOT make sense for unordered data because
# the previous row may have no meaningful relationship with
# the missing value.
df5["Temperature"] = df5["Temperature"].ffill()

print("\nDataFrame after forward fill:")
print(df5)