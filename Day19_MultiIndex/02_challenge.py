import pandas as pd

# =========================================================
# DATASET: 3 YEARS × 4 QUARTERS = 12 ROWS
# =========================================================

sales = pd.DataFrame({
    "Year": [
        2022, 2022, 2022, 2022,
        2023, 2023, 2023, 2023,
        2024, 2024, 2024, 2024
    ],
    "Quarter": [
        "Q1", "Q2", "Q3", "Q4",
        "Q1", "Q2", "Q3", "Q4",
        "Q1", "Q2", "Q3", "Q4"
    ],
    "Revenue": [
        50000, 60000, 55000, 70000,
        65000, 72000, 68000, 80000,
        75000, 85000, 90000, 95000
    ]
})

print("=" * 75)
print("ORIGINAL SALES DATA")
print("=" * 75)
print(sales)


# =========================================================
# 1. SET YEAR AND QUARTER AS MULTIINDEX
# =========================================================

print("\n" + "=" * 75)
print("1. MULTIINDEX SALES DATA")
print("=" * 75)

multi_sales = sales.set_index(["Year", "Quarter"])

print(multi_sales)


# =========================================================
# 2. RETRIEVE ALL DATA FOR A SPECIFIC YEAR
# Using loc[]
#
# Retrieve all quarters for 2023
# =========================================================

print("\n" + "=" * 75)
print("2. ALL DATA FOR YEAR 2023")
print("=" * 75)

sales_2023 = multi_sales.loc[2023]

print(sales_2023)


# =========================================================
# 3. RETRIEVE Q1 DATA ACROSS ALL YEARS
# Using xs()
#
# level="Quarter" searches the inner index level
# =========================================================

print("\n" + "=" * 75)
print("3. Q1 DATA ACROSS ALL YEARS")
print("=" * 75)

q1_sales = multi_sales.xs(
    "Q1",
    level="Quarter"
)

print(q1_sales)


# =========================================================
# 4. TOTAL REVENUE PER YEAR
# Group by the outer MultiIndex level
# =========================================================

print("\n" + "=" * 75)
print("4. TOTAL REVENUE PER YEAR")
print("=" * 75)

yearly_summary = (
    multi_sales
    .groupby(level="Year")["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Year")
    .reset_index(drop=True)
)

print(yearly_summary)


# =========================================================
# 5. FLATTENED AND SORTED SUMMARY TABLE
# Ensure a clean column structure
# =========================================================

print("\n" + "=" * 75)
print("5. FINAL FLATTENED SORTED SUMMARY")
print("=" * 75)

yearly_summary.columns = ["Year", "TotalRevenue"]

print(yearly_summary)