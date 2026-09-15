import pandas as pd

# ============================================================
# 1. EASY — LONG FORMAT → WIDE FORMAT USING pivot()
# ============================================================

sales = pd.DataFrame({
    "Date": [
        "2025-01-01", "2025-01-01", "2025-01-01",
        "2025-01-02", "2025-01-02", "2025-01-02"
    ],
    "Product": [
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet"
    ],
    "Sales": [
        50000, 30000, 20000,
        55000, 35000, 25000
    ]
})

wide_sales = sales.pivot(
    index="Date",
    columns="Product",
    values="Sales"
).reset_index()

print("=" * 70)
print("1. PIVOT — LONG TO WIDE")
print("=" * 70)
print(wide_sales)


# ============================================================
# 2. EASY — WIDE FORMAT → LONG FORMAT USING melt()
# ============================================================

monthly_sales = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "January": [50000, 30000, 20000],
    "February": [55000, 35000, 25000],
    "March": [60000, 40000, 30000]
})

long_sales = monthly_sales.melt(
    id_vars="Product",
    var_name="Month",
    value_name="Sales"
)

print("\n" + "=" * 70)
print("2. MELT — WIDE TO LONG")
print("=" * 70)
print(long_sales)


# ============================================================
# 3. MEDIUM — DUPLICATE INDEX/COLUMN COMBINATIONS
# ============================================================

duplicate_sales = pd.DataFrame({
    "Date": [
        "2025-01-01",
        "2025-01-01",   # Duplicate Date + Product combination
        "2025-01-01",
        "2025-01-02",
        "2025-01-02"
    ],
    "Product": [
        "Laptop",
        "Laptop",       # Duplicate
        "Phone",
        "Laptop",
        "Phone"
    ],
    "Sales": [
        50000,
        10000,
        30000,
        55000,
        35000
    ]
})

# ------------------------------------------------------------
# Attempt pivot()
# ------------------------------------------------------------

try:
    duplicate_wide = duplicate_sales.pivot(
        index="Date",
        columns="Product",
        values="Sales"
    )

    print("\nPivot result:")
    print(duplicate_wide)

except ValueError as e:
    print("\n" + "=" * 70)
    print("3. PIVOT ERROR")
    print("=" * 70)
    print("pivot() cannot handle duplicate Date + Product combinations.")
    print("Error:", e)


# ------------------------------------------------------------
# Correct solution: pivot_table()
# ------------------------------------------------------------

duplicate_wide_sum = duplicate_sales.pivot_table(
    index="Date",
    columns="Product",
    values="Sales",
    aggfunc="sum"
).reset_index()

print("\n" + "=" * 70)
print("3. PIVOT_TABLE — SUM")
print("=" * 70)
print(duplicate_wide_sum)

# For 2025-01-01 + Laptop:
# 50,000 + 10,000 = 60,000
#
# pivot() fails because there are TWO values for the
# same Date + Product combination.
#
# pivot_table() solves this by aggregating them.


# ============================================================
# 4. MEDIUM — COMPARE mean VS sum
# ============================================================

mean_table = duplicate_sales.pivot_table(
    index="Date",
    columns="Product",
    values="Sales",
    aggfunc="mean"
).reset_index()

sum_table = duplicate_sales.pivot_table(
    index="Date",
    columns="Product",
    values="Sales",
    aggfunc="sum"
).reset_index()

print("\n" + "=" * 70)
print("4A. PIVOT_TABLE — MEAN")
print("=" * 70)
print(mean_table)

print("\n" + "=" * 70)
print("4B. PIVOT_TABLE — SUM")
print("=" * 70)
print(sum_table)

# Comparison:
#
# For 2025-01-01 + Laptop:
#
# SUM  = (50,000 + 10,000) = 60,000
# MEAN = (50,000 + 10,000) / 2 = 30,000
#
# SUM gives the combined/total sales.
# MEAN gives the average sales for that combination.


# ============================================================
# 5. CHALLENGING
# WIDE QUARTERLY SALES → LONG → GROUPBY → WIDE
# ============================================================

quarterly_sales = pd.DataFrame({
    "Product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Headphones"
    ],
    "Q1": [50000, 30000, 20000, 15000],
    "Q2": [55000, 35000, 25000, 18000],
    "Q3": [60000, 40000, 30000, 20000],
    "Q4": [65000, 45000, 35000, 22000]
})

print("\n" + "=" * 70)
print("5A. ORIGINAL QUARTERLY DATA")
print("=" * 70)
print(quarterly_sales)


# ------------------------------------------------------------
# Step 1: Melt wide → long
# ------------------------------------------------------------

quarterly_long = quarterly_sales.melt(
    id_vars="Product",
    var_name="Quarter",
    value_name="Sales"
)

print("\n" + "=" * 70)
print("5B. MELTED QUARTERLY DATA")
print("=" * 70)
print(quarterly_long)


# ------------------------------------------------------------
# Step 2: Average sales per quarter across products
# ------------------------------------------------------------

quarter_average = (
    quarterly_long
    .groupby("Quarter")["Sales"]
    .mean()
    .sort_values(ascending=False)
)

print("\n" + "=" * 70)
print("5C. AVERAGE SALES BY QUARTER")
print("=" * 70)
print(quarter_average)


# ------------------------------------------------------------
# Step 3: Find quarter with highest average sales
# ------------------------------------------------------------

best_quarter = quarter_average.idxmax()
best_average = quarter_average.max()

print("\nHighest average sales quarter:", best_quarter)
print("Average sales:", best_average)


# ------------------------------------------------------------
# Step 4: Pivot back to wide format
# Product = rows
# Quarter = columns
# Sales = values
# ------------------------------------------------------------

quarterly_wide_summary = quarterly_long.pivot(
    index="Product",
    columns="Quarter",
    values="Sales"
).reset_index()

print("\n" + "=" * 70)
print("5D. FINAL WIDE SUMMARY")
print("=" * 70)
print(quarterly_wide_summary)