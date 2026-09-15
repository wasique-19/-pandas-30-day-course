import pandas as pd
import numpy as np


# ------------------------------------------------------------
# Create a DataFrame with 8 products
# ------------------------------------------------------------

df = pd.DataFrame({
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Headphones", "Printer", "Webcam", "Speaker"
    ],

    "Price": [
        55000, np.nan, 2500, 18000,
        np.nan, 12000, 4500, 3000
    ],

    "Category": [
        "Electronics", "Accessories", np.nan, "Electronics",
        "Accessories", "Electronics", np.nan, "Accessories"
    ],

    "LastRestocked": [
        "2026-01-10", np.nan, "2026-02-15", "2026-03-01",
        np.nan, "2026-03-20", "2026-04-05", np.nan
    ]
})


# Convert LastRestocked into a date column
df["LastRestocked"] = pd.to_datetime(df["LastRestocked"])


# ------------------------------------------------------------
# Missing values BEFORE cleaning
# ------------------------------------------------------------

print("Missing values BEFORE cleaning:")
print(df.isna().sum())


# ------------------------------------------------------------
# Clean Price
# ------------------------------------------------------------

# Median is suitable for Price because it is numeric and is
# less affected by unusually high or low prices than the mean.
df["Price"] = df["Price"].fillna(df["Price"].median())


# ------------------------------------------------------------
# Clean Category
# ------------------------------------------------------------

# Mode is suitable for Category because it is categorical data,
# so the most frequently occurring category is a reasonable choice.
df["Category"] = df["Category"].fillna(df["Category"].mode()[0])


# ------------------------------------------------------------
# Clean LastRestocked
# ------------------------------------------------------------

# Forward fill is suitable because the products are listed in
# a meaningful order, so a missing restock date can use the
# most recently available date.
df["LastRestocked"] = df["LastRestocked"].ffill()


# ------------------------------------------------------------
# Display cleaned DataFrame
# ------------------------------------------------------------

print("\nCleaned DataFrame:")
print(df)


# ------------------------------------------------------------
# Missing values AFTER cleaning
# ------------------------------------------------------------

print("\nMissing values AFTER cleaning:")
print(df.isna().sum())