import pandas as pd

# ---------------------------------------------------------
# DATASET
# ---------------------------------------------------------

sales = pd.DataFrame({
    "Region": [
        "North", "North", "North", "North",
        "South", "South", "South",
        "West", "West", "West", "West"
    ],
    "Category": [
        "Electronics", "Furniture", "Electronics", "Furniture",
        "Electronics", "Furniture", "Electronics",
        "Electronics", "Furniture", "Electronics", "Furniture"
    ],
    "Sales": [
        50000, 30000, 45000, 25000,
        40000, 20000, 35000,
        60000, 30000, 55000, 25000
    ]
})

print("=" * 70)
print("ORIGINAL DATA")
print("=" * 70)
print(sales)


# =========================================================
# 1. EASY
# Crosstab: Count records for each combination
# =========================================================

print("\n" + "=" * 70)
print("1. CROSSTAB - COUNT")
print("=" * 70)

count_table = pd.crosstab(
    sales["Region"],
    sales["Category"]
)

print(count_table)


# =========================================================
# 2. EASY
# Crosstab with margins=True
# Adds row totals and column totals
# =========================================================

print("\n" + "=" * 70)
print("2. CROSSTAB - COUNT WITH TOTALS")
print("=" * 70)

count_with_totals = pd.crosstab(
    sales["Region"],
    sales["Category"],
    margins=True
)

print(count_with_totals)


# =========================================================
# 3. MEDIUM
# Crosstab that SUMS a numeric column
# values = numeric column
# aggfunc = aggregation function
# =========================================================

print("\n" + "=" * 70)
print("3. CROSSTAB - SUM OF SALES")
print("=" * 70)

sales_crosstab = pd.crosstab(
    sales["Region"],
    sales["Category"],
    values=sales["Sales"],
    aggfunc="sum"
)

print(sales_crosstab)


# =========================================================
# 4. MEDIUM
# normalize="index"
# Shows row-wise percentages
#
# IMPORTANT:
# Each row will sum to 1.0 (100%).
# =========================================================

print("\n" + "=" * 70)
print("4. CROSSTAB - ROW-WISE PERCENTAGES")
print("=" * 70)

percentage_table = pd.crosstab(
    sales["Region"],
    sales["Category"],
    normalize="index"
)

print(percentage_table)

print("\nAs percentages:")
print((percentage_table * 100).round(2))


# =========================================================
# 5. CHALLENGING
# Pivot table:
# - Two aggregation functions: sum and mean
# - Same value column: Sales
# - margins=True
# - fill_value=0
# - Flatten MultiIndex columns
# =========================================================

print("\n" + "=" * 70)
print("5. PIVOT TABLE - SUM + MEAN")
print("=" * 70)

pivot_summary = pd.pivot_table(
    sales,
    index="Region",
    columns="Category",
    values="Sales",
    aggfunc=["sum", "mean"],
    margins=True,
    fill_value=0
)

print("Before flattening columns:")
print(pivot_summary)


# ---------------------------------------------------------
# FLATTEN MULTIINDEX COLUMNS
# ---------------------------------------------------------

pivot_summary.columns = [
    "_".join(str(x) for x in col if str(x) != "")
    for col in pivot_summary.columns
]

# Make the index a normal column
pivot_summary = pivot_summary.reset_index()

print("\nAfter flattening columns:")
print(pivot_summary)


# =========================================================
# FINAL OUTPUT
# =========================================================

print("\n" + "=" * 70)
print("FINAL PIVOT TABLE")
print("=" * 70)
print(pivot_summary)