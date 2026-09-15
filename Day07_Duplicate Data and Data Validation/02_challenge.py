import pandas as pd

# ============================================================
# CHALLENGE: ORDER DATA CLEANING
# ============================================================

# ------------------------------------------------------------
# 1. Create raw Order DataFrame
# ------------------------------------------------------------

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 102, 105, 106, 107, 108],
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Mouse", "Phone", "Tablet", "Printer", "Headphones"
    ],
    "Region": [
        "north", "South", "NORTH", "east",
        "south", "WEST", "North", "EAST", "south"
    ],
    "Quantity": [2, 5, 3, 1, 4, -2, 6, 2, 8]
})

# ------------------------------------------------------------
# 2. BEFORE CLEANING
# ------------------------------------------------------------

print("=" * 65)
print("BEFORE CLEANING")
print("=" * 65)

print(orders)

print("\nShape before cleaning:", orders.shape)

# Check duplicate OrderIDs
print("\nDuplicate OrderIDs:")
print(orders[orders.duplicated(subset=["OrderID"], keep=False)])

# Check inconsistent Region values
print("\nRegion values before standardization:")
print(orders["Region"].unique())

# Check invalid negative Quantity
print("\nInvalid Quantity rows:")
print(orders[orders["Quantity"] < 0])


# ============================================================
# CLEANING PROCESS
# ============================================================

# ------------------------------------------------------------
# 3. Deduplicate by OrderID
#    Keep the first occurrence
# ------------------------------------------------------------

orders = orders.drop_duplicates(
    subset=["OrderID"],
    keep="first"
).copy()


# ------------------------------------------------------------
# 4. Standardize Region casing
#    north, North, NORTH -> North
#    south, South, SOUTH -> South
# ------------------------------------------------------------

orders["Region"] = (
    orders["Region"]
    .str.strip()
    .str.title()
)


# ------------------------------------------------------------
# 5. Flag invalid negative Quantity
# ------------------------------------------------------------

orders["InvalidQuantity"] = orders["Quantity"] < 0

print("\n" + "=" * 65)
print("INVALID QUANTITY FLAG")
print("=" * 65)

print(orders[orders["InvalidQuantity"]])


# ------------------------------------------------------------
# 6. Remove rows with negative Quantity
# ------------------------------------------------------------

orders = orders[
    orders["Quantity"] >= 0
].copy()


# ------------------------------------------------------------
# 7. Remove helper column
# ------------------------------------------------------------

orders = orders.drop(columns=["InvalidQuantity"])


# ============================================================
# FINAL VALIDATION
# ============================================================

print("\n" + "=" * 65)
print("AFTER CLEANING")
print("=" * 65)

print(orders)

print("\nShape after cleaning:", orders.shape)

# Check whether OrderIDs are still duplicated
print("\nDuplicate OrderIDs after cleaning:")
print(orders["OrderID"].duplicated().any())

# Check standardized Region values
print("\nRegion values after cleaning:")
print(orders["Region"].unique())

# Check for negative quantities
print("\nNegative Quantity exists:")
print((orders["Quantity"] < 0).any())


# ============================================================
# FINAL CLEAN DATAFRAME
# ============================================================

print("\n" + "=" * 65)
print("FINAL CLEAN DATAFRAME")
print("=" * 65)

print(orders.to_string(index=False))