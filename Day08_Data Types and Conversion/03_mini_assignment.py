import pandas as pd

# ============================================================
# 12. MINI ASSIGNMENT
# RAW PRODUCT EXPORT CLEANING
# ============================================================

print("=" * 75)
print("12. MINI ASSIGNMENT - PRODUCT DATA CLEANING")
print("=" * 75)


# ============================================================
# STEP 1: CREATE RAW / MESSY DATAFRAME
# ============================================================

products = pd.DataFrame({
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Phone", "Tablet", "Headphones", "Webcam",
        "Printer", "Speaker", "USB Cable", "Power Bank",
        "Smartwatch", "Charger", "SSD", "Router",
        "Microphone", "Desk Lamp", "Mouse Pad", "Camera"
    ],

    "Price": [
        "$1,200", "$25", "$75", "$350",
        "$800", "$450", "$120", "$90",
        "$250", "$150", "$15", "$60",
        "$200", "$40", "$180", "$110",
        "$130", "$55", "$20", "$500"
    ],

    "InStock": [
        "Yes", "No", "Yes", "Yes",
        "No", "Yes", "Yes", "No",
        "Yes", "No", "Yes", "Yes",
        "No", "Yes", "Yes", "No",
        "Yes", "No", "Yes", "Yes"
    ],

    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Electronics", "Accessories", "Accessories",
        "Office", "Electronics", "Accessories", "Accessories",
        "Electronics", "Accessories", "Electronics", "Electronics",
        "Electronics", "Office", "Accessories", "Electronics"
    ]
})


# ============================================================
# STEP 2: DISPLAY RAW DATA
# ============================================================

print("\nRAW DATA:")
print(products)


# ============================================================
# STEP 3: CHECK DTYPES BEFORE CLEANING
# ============================================================

print("\n" + "=" * 75)
print("DTYPES BEFORE CLEANING")
print("=" * 75)

print(products.dtypes)


# ============================================================
# STEP 4: CHECK CATEGORY MEMORY BEFORE CONVERSION
# ============================================================

print("\n" + "=" * 75)
print("CATEGORY MEMORY BEFORE CONVERSION")
print("=" * 75)

memory_before = products["Category"].memory_usage(deep=True)

print("Memory usage before:", memory_before, "bytes")


# ============================================================
# STEP 5: CLEAN PRICE
#
# "$1,200" -> "1200" -> 1200.0
#
# Remove:
#   $  = currency symbol
#   ,  = thousands separator
# ============================================================

products["Price"] = (
    products["Price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

products["Price"] = pd.to_numeric(products["Price"])


# ============================================================
# STEP 6: CONVERT INSTOCK
#
# Yes -> True
# No  -> False
#
# map() is appropriate because we want explicit
# Yes/No conversion.
# ============================================================

products["InStock"] = products["InStock"].map({
    "Yes": True,
    "No": False
})


# ============================================================
# STEP 7: CONVERT CATEGORY TO CATEGORY DTYPE
# ============================================================

products["Category"] = products["Category"].astype("category")


# ============================================================
# STEP 8: CHECK CATEGORY MEMORY AFTER CONVERSION
# ============================================================

memory_after = products["Category"].memory_usage(deep=True)

print("\n" + "=" * 75)
print("CATEGORY MEMORY AFTER CONVERSION")
print("=" * 75)

print("Memory usage after:", memory_after, "bytes")


# ============================================================
# STEP 9: MEMORY COMPARISON
# ============================================================

memory_saved = memory_before - memory_after

print("\n" + "=" * 75)
print("MEMORY COMPARISON")
print("=" * 75)

print("Memory before :", memory_before, "bytes")
print("Memory after  :", memory_after, "bytes")
print("Memory saved  :", memory_saved, "bytes")

if memory_before > 0:
    reduction = (memory_saved / memory_before) * 100
    print("Reduction     :", round(reduction, 2), "%")


# ============================================================
# STEP 10: FINAL CLEANED DATAFRAME
# ============================================================

print("\n" + "=" * 75)
print("FINAL CLEANED DATAFRAME")
print("=" * 75)

print(products)


# ============================================================
# STEP 11: DTYPES AFTER CLEANING
# ============================================================

print("\n" + "=" * 75)
print("DTYPES AFTER CLEANING")
print("=" * 75)

print(products.dtypes)


# ============================================================
# STEP 12: VERIFY CATEGORY VALUES
# ============================================================

print("\n" + "=" * 75)
print("CATEGORY INFORMATION")
print("=" * 75)

print("Unique categories:")
print(products["Category"].unique())

print("\nNumber of unique categories:")
print(products["Category"].nunique())

print("\nCategory dtype:")
print(products["Category"].dtype)