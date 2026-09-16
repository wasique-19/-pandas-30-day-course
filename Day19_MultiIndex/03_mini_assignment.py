import pandas as pd

# =========================================================
# DATASET
# 2 COUNTRIES × 2 CITIES EACH
# =========================================================

sales = pd.DataFrame({
    "Country": [
        "India", "India",
        "USA", "USA"
    ],
    "City": [
        "Delhi", "Mumbai",
        "New York", "Chicago"
    ],
    "Revenue": [
        85000, 72000,
        95000, 68000
    ]
})

print("=" * 70)
print("ORIGINAL SALES DATA")
print("=" * 70)
print(sales)


# =========================================================
# 1. SET COUNTRY AND CITY AS MULTIINDEX
# =========================================================

print("\n" + "=" * 70)
print("1. MULTIINDEX SALES DATA")
print("=" * 70)

multi_sales = sales.set_index(["Country", "City"])

print(multi_sales)


# =========================================================
# 2. SELECT ALL DATA FOR ONE COUNTRY USING loc[]
# Select all cities in India
# =========================================================

print("\n" + "=" * 70)
print("2. ALL DATA FOR INDIA")
print("=" * 70)

india_sales = multi_sales.loc["India"]

print(india_sales)


# =========================================================
# 3. USE xs() TO COMPARE ONE CITY ACROSS BOTH COUNTRIES
#
# IMPORTANT:
# The same city must exist in both countries.
# Therefore, create a comparison dataset with
# New York in both countries.
# =========================================================

print("\n" + "=" * 70)
print("3. CITY COMPARISON USING xs()")
print("=" * 70)

comparison_data = pd.DataFrame({
    "Country": [
        "India", "India",
        "USA", "USA"
    ],
    "City": [
        "New York", "Mumbai",
        "New York", "Chicago"
    ],
    "Revenue": [
        78000, 72000,
        95000, 68000
    ]
})

comparison_multi = comparison_data.set_index(
    ["Country", "City"]
)

# Select New York from every country
new_york_sales = comparison_multi.xs(
    "New York",
    level="City"
)

print(new_york_sales)


# =========================================================
# 4. RESET INDEX TO CREATE A FLAT DATAFRAME
# =========================================================

print("\n" + "=" * 70)
print("4. RESET INDEX")
print("=" * 70)

flat_sales = multi_sales.reset_index()

print(flat_sales)


# =========================================================
# 5. SORT FINAL FLAT SUMMARY BY REVENUE DESCENDING
# =========================================================

print("\n" + "=" * 70)
print("5. FINAL FLAT SUMMARY SORTED BY REVENUE")
print("=" * 70)

final_summary = (
    flat_sales
    .sort_values(by="Revenue", ascending=False)
    .reset_index(drop=True)
)

print(final_summary)