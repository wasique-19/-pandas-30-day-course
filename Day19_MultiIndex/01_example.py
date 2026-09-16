import pandas as pd

# =========================================================
# DATAFRAME
# =========================================================

sales = pd.DataFrame({
    "Region": [
        "North", "North", "North",
        "South", "South", "South",
        "West", "West", "West"
    ],
    "Product": [
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet"
    ],
    "Sales": [
        50000, 30000, 20000,
        45000, 35000, 25000,
        60000, 40000, 30000
    ],
    "Units": [
        10, 15, 8,
        9, 18, 10,
        12, 20, 14
    ]
})

print("=" * 70)
print("ORIGINAL DATAFRAME")
print("=" * 70)
print(sales)


# =========================================================
# 1. EASY
# Set two columns as a MultiIndex using set_index()
# =========================================================

print("\n" + "=" * 70)
print("1. MULTIINDEX DATAFRAME")
print("=" * 70)

multi_sales = sales.set_index(["Region", "Product"])

print(multi_sales)


# =========================================================
# 2. EASY
# Select all rows belonging to one outer-level value
# Using loc[]
#
# Select all products from the North region
# =========================================================

print("\n" + "=" * 70)
print("2. SELECT ALL ROWS FROM NORTH")
print("=" * 70)

north_sales = multi_sales.loc["North"]

print(north_sales)


# =========================================================
# 3. MEDIUM
# Select a specific combination of both index levels
# Using tuple-based loc[]
#
# Select North + Laptop
# =========================================================

print("\n" + "=" * 70)
print("3. SELECT NORTH + LAPTOP")
print("=" * 70)

north_laptop = multi_sales.loc[("North", "Laptop")]

print(north_laptop)


# =========================================================
# 4. MEDIUM
# Use xs() to select based on the INNER index level
# across all outer-level groups
#
# Select Laptop from every region
# =========================================================

print("\n" + "=" * 70)
print("4. SELECT LAPTOP FROM ALL REGIONS USING xs()")
print("=" * 70)

laptop_sales = multi_sales.xs(
    "Laptop",
    level="Product"
)

print(laptop_sales)


# =========================================================
# 5. CHALLENGING
# Swap MultiIndex levels
# Sort the result
# Reset index to create a flat DataFrame
# Compare column order with the original
# =========================================================

print("\n" + "=" * 70)
print("5A. SWAP INDEX LEVELS")
print("=" * 70)

swapped_sales = multi_sales.swaplevel(
    "Region",
    "Product"
)

print(swapped_sales)


print("\n" + "=" * 70)
print("5B. SORT AFTER SWAPPING LEVELS")
print("=" * 70)

sorted_swapped_sales = swapped_sales.sort_index()

print(sorted_swapped_sales)


print("\n" + "=" * 70)
print("5C. RESET INDEX TO CREATE FLAT DATAFRAME")
print("=" * 70)

flat_sales = sorted_swapped_sales.reset_index()

print(flat_sales)


# =========================================================
# COLUMN ORDER COMPARISON
# =========================================================

print("\n" + "=" * 70)
print("COLUMN ORDER COMPARISON")
print("=" * 70)

print("Original columns:")
print(list(sales.columns))

print("\nFlat DataFrame columns after swaplevel + reset_index:")
print(list(flat_sales.columns))