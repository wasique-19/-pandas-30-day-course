import pandas as pd
import numpy as np

# ============================================================
# 1. CREATE A 50-ROW SIMULATED DATASET
# ============================================================

np.random.seed(42)

n = 50

df = pd.DataFrame({
    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        size=n
    ),

    "Category": np.random.choice(
        ["Electronics", "Furniture", "Clothing"],
        size=n
    ),

    "Sales": np.random.randint(
        1000, 10000, size=n
    ),

    "Quantity": np.random.randint(
        1, 50, size=n
    ),

    "Rating": np.round(
        np.random.uniform(2.5, 5.0, size=n),
        2
    )
})

print("=" * 70)
print("FULL EDA REPORT")
print("=" * 70)


# ============================================================
# 2. DATASET UNDERSTANDING
# ============================================================

print("\n" + "=" * 70)
print("1. DATASET UNDERSTANDING")
print("=" * 70)

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nDataset information:")
df.info()

print("\nDescriptive statistics:")
print(df.describe())


# ============================================================
# 3. DATA QUALITY CHECKS
# ============================================================

print("\n" + "=" * 70)
print("2. DATA QUALITY CHECKS")
print("=" * 70)

print("\nMissing values:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nUnique values in categorical columns:")
print("\nRegion:")
print(df["Region"].unique())

print("\nCategory:")
print(df["Category"].unique())

# Check for invalid numeric values
print("\nInvalid Sales values:")
print((df["Sales"] < 0).sum())

print("\nInvalid Quantity values:")
print((df["Quantity"] <= 0).sum())

print("\nInvalid Rating values:")
print(
    ((df["Rating"] < 1) | (df["Rating"] > 5)).sum()
)


# ============================================================
# 4. UNIVARIATE STATISTICS
# ============================================================

print("\n" + "=" * 70)
print("3. UNIVARIATE ANALYSIS")
print("=" * 70)

numeric_columns = [
    "Sales",
    "Quantity",
    "Rating"
]

for column in numeric_columns:

    print(f"\n--- {column} ---")

    print(f"Mean     : {df[column].mean():.2f}")
    print(f"Median   : {df[column].median():.2f}")
    print(f"Minimum  : {df[column].min():.2f}")
    print(f"Maximum  : {df[column].max():.2f}")
    print(f"Std Dev  : {df[column].std():.2f}")
    print(f"Skewness : {df[column].skew():.2f}")


# ============================================================
# 5. BIVARIATE GROUPBY ANALYSIS
#    REGION vs SALES
# ============================================================

print("\n" + "=" * 70)
print("4. BIVARIATE ANALYSIS")
print("Region vs Sales")
print("=" * 70)

region_summary = (
    df.groupby("Region")
      .agg(
          TotalSales=("Sales", "sum"),
          AverageSales=("Sales", "mean"),
          AverageQuantity=("Quantity", "mean"),
          NumberOfRecords=("Sales", "count")
      )
      .reset_index()
)

region_summary[
    ["TotalSales", "AverageSales", "AverageQuantity"]
] = region_summary[
    ["TotalSales", "AverageSales", "AverageQuantity"]
].round(2)

print(region_summary.to_string(index=False))


# ============================================================
# 6. SECOND GROUPBY COMPARISON
#    CATEGORY vs SALES
# ============================================================

print("\n" + "=" * 70)
print("Category vs Sales")
print("=" * 70)

category_summary = (
    df.groupby("Category")
      .agg(
          TotalSales=("Sales", "sum"),
          AverageSales=("Sales", "mean"),
          AverageRating=("Rating", "mean"),
          Records=("Sales", "count")
      )
      .reset_index()
)

category_summary[
    ["TotalSales", "AverageSales", "AverageRating"]
] = category_summary[
    ["TotalSales", "AverageSales", "AverageRating"]
].round(2)

print(category_summary.to_string(index=False))


# ============================================================
# 7. CORRELATION MATRIX
# ============================================================

print("\n" + "=" * 70)
print("5. CORRELATION MATRIX")
print("=" * 70)

correlation = df[
    ["Sales", "Quantity", "Rating"]
].corr()

print(correlation.round(3))


# ============================================================
# 8. FIND STRONGEST CORRELATION
# ============================================================

upper_triangle = correlation.where(
    np.triu(
        np.ones(correlation.shape),
        k=1
    ).astype(bool)
)

correlation_pairs = (
    upper_triangle
    .stack()
    .sort_values(
        key=lambda x: abs(x),
        ascending=False
    )
)

strongest_pair = correlation_pairs.index[0]
strongest_value = correlation_pairs.iloc[0]

print("\nStrongest relationship:")
print(
    f"{strongest_pair[0]} vs {strongest_pair[1]} "
    f"= {strongest_value:.3f}"
)


# ============================================================
# 9. PREPARE VALUES FOR BUSINESS INSIGHTS
# ============================================================

highest_region = region_summary.loc[
    region_summary["AverageSales"].idxmax()
]

lowest_region = region_summary.loc[
    region_summary["AverageSales"].idxmin()
]

highest_category = category_summary.loc[
    category_summary["AverageSales"].idxmax()
]


# ============================================================
# 10. EXACTLY 3 BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("6. BUSINESS INSIGHTS")
print("=" * 70)

print(
    f"1. {highest_region['Region']} has the highest average "
    f"sales per record at {highest_region['AverageSales']:.2f}, "
    f"indicating stronger transaction-level sales performance "
    f"than the other regions in this dataset."
)

print(
    f"2. {highest_category['Category']} has the highest average "
    f"sales at {highest_category['AverageSales']:.2f}, suggesting "
    f"that this category generates larger sales per record and "
    f"could be examined for successful products or sales practices."
)

print(
    f"3. {strongest_pair[0]} and {strongest_pair[1]} show the "
    f"strongest observed correlation of {strongest_value:.3f}, "
    f"indicating that these measures tend to move together; "
    f"however, the correlation does not by itself establish causation."
)