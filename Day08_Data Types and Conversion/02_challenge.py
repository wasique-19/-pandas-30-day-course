import pandas as pd

# ============================================================
# 8. CHALLENGE QUESTION
# CLEAN SALES EXPORT + MEMORY COMPARISON
# ============================================================

print("=" * 75)
print("8. SALES DATA CLEANING CHALLENGE")
print("=" * 75)


# ============================================================
# STEP 1: RAW / MESSY DATASET
# ============================================================

sales = pd.DataFrame({
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    
    "Product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Monitor",
        "Keyboard",
        "Headphones",
        "Mouse",
        "Printer"
    ],
    
    "Revenue": [
        "$1,200",
        "$2,500",
        "$850",
        "$1,750",
        "$450",
        "$1,050",
        "$275",
        "$3,200"
    ],
    
    "Discount": [
        "10%",
        "5%",
        "n/a",
        "15%",
        "20%",
        "invalid",
        "10%",
        "n/a"
    ],
    
    "SalesRegion": [
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
        "East",
        "West"
    ]
})


print("\nRAW DATA:")
print(sales)


# ============================================================
# STEP 2: CHECK DATA TYPES BEFORE CLEANING
# ============================================================

print("\n" + "=" * 75)
print("DATA TYPES BEFORE CLEANING")
print("=" * 75)

print(sales.dtypes)


# ============================================================
# STEP 3: MEMORY USAGE BEFORE CHANGES
# ============================================================

print("\n" + "=" * 75)
print("MEMORY USAGE BEFORE CHANGES")
print("=" * 75)

memory_before = sales.memory_usage(deep=True)

print(memory_before)

print("\nTotal memory before:")
print(memory_before.sum(), "bytes")


# ============================================================
# STEP 4: CLEAN REVENUE
# Remove $ and comma
# Then convert text -> numeric
# ============================================================

sales["Revenue"] = (
    sales["Revenue"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

sales["Revenue"] = pd.to_numeric(sales["Revenue"])


# ============================================================
# STEP 5: CLEAN DISCOUNT
# Remove % sign
# Invalid values become NaN using errors="coerce"
# ============================================================

sales["Discount"] = (
    sales["Discount"]
    .str.replace("%", "", regex=False)
)

sales["Discount"] = pd.to_numeric(
    sales["Discount"],
    errors="coerce"
)


# ============================================================
# STEP 6: CONVERT SALESREGION TO CATEGORY
# ============================================================

sales["SalesRegion"] = sales["SalesRegion"].astype("category")


# ============================================================
# STEP 7: MEMORY USAGE AFTER CHANGES
# ============================================================

print("\n" + "=" * 75)
print("MEMORY USAGE AFTER CHANGES")
print("=" * 75)

memory_after = sales.memory_usage(deep=True)

print(memory_after)

print("\nTotal memory after:")
print(memory_after.sum(), "bytes")


# ============================================================
# STEP 8: MEMORY SAVED
# ============================================================

memory_saved = memory_before.sum() - memory_after.sum()

print("\n" + "=" * 75)
print("MEMORY COMPARISON")
print("=" * 75)

print("Memory before :", memory_before.sum(), "bytes")
print("Memory after  :", memory_after.sum(), "bytes")
print("Memory saved  :", memory_saved, "bytes")

if memory_before.sum() > 0:
    reduction = (memory_saved / memory_before.sum()) * 100
    print("Reduction     :", round(reduction, 2), "%")


# ============================================================
# STEP 9: FINAL CLEANED DATAFRAME
# ============================================================

print("\n" + "=" * 75)
print("FINAL CLEANED DATAFRAME")
print("=" * 75)

print(sales)


# ============================================================
# STEP 10: FINAL DATA TYPES
# ============================================================

print("\n" + "=" * 75)
print("FINAL DATA TYPES")
print("=" * 75)

print(sales.dtypes)


# ============================================================
# STEP 11: CHECK UNIQUE REGIONS
# ============================================================

print("\n" + "=" * 75)
print("SALES REGION INFORMATION")
print("=" * 75)

print("Unique regions:")
print(sales["SalesRegion"].unique())

print("\nNumber of unique regions:")
print(sales["SalesRegion"].nunique())

print("\nSalesRegion dtype:")
print(sales["SalesRegion"].dtype)


# ============================================================
# STEP 12: CHECK INVALID DISCOUNTS
# ============================================================

print("\n" + "=" * 75)
print("DISCOUNT AFTER CONVERSION")
print("=" * 75)

print(sales["Discount"])

print("\nNumber of invalid/missing discounts:")
print(sales["Discount"].isna().sum())