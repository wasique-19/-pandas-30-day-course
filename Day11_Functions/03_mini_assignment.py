import pandas as pd

# ============================================================
# 1. CREATE DATAFRAME
# ============================================================

products = pd.DataFrame({
    "Product": [
        "Laptop", "Rice", "Shampoo", "Mobile", 
        "Headphones", "Wheat", "Soap", "Monitor"
    ],
    "Price": [
        60000, 2500, 350, 30000,
        2500, 2200, 120, 18000
    ],
    "Category": [
        "EL", "FD", "CL", "EL",
        "EL", "FD", "CL", "EL"
    ],
    "StockQty": [
        3, 15, 8, 2,
        20, 5, 30, 7
    ]
})

print("ORIGINAL DATA")
print(products)


# ============================================================
# 2. CREATE CUSTOM FUNCTION FOR RESTOCK PRIORITY
# ============================================================

def restock_priority(row):

    category = row["Category"]
    stock = row["StockQty"]

    # --------------------------------------------------------
    # Electronics (EL)
    # High-value items -> restock quickly
    # --------------------------------------------------------
    if category == "EL":

        if stock <= 3:
            return "Urgent"

        elif stock <= 7:
            return "Soon"

        else:
            return "Not Needed"

    # --------------------------------------------------------
    # Food (FD)
    # Food requires higher stock levels
    # --------------------------------------------------------
    elif category == "FD":

        if stock <= 5:
            return "Urgent"

        elif stock <= 10:
            return "Soon"

        else:
            return "Not Needed"

    # --------------------------------------------------------
    # Clothing (CL)
    # --------------------------------------------------------
    elif category == "CL":

        if stock <= 5:
            return "Urgent"

        elif stock <= 10:
            return "Soon"

        else:
            return "Not Needed"

    # If category is unknown
    else:
        return "Not Needed"


# ============================================================
# 3. APPLY FUNCTION ROW-WISE
# ============================================================

products["RestockPriority"] = products.apply(
    restock_priority,
    axis=1
)


# ============================================================
# 4. USE map() TO CONVERT CATEGORY CODES
# ============================================================

category_map = {
    "EL": "Electronics",
    "FD": "Food",
    "CL": "Clothing"
}

# Create a friendly display column
products["CategoryName"] = products["Category"].map(category_map)


# ============================================================
# 5. PRINT FINAL DATAFRAME
# ============================================================

print("\n" + "=" * 90)
print("FINAL PRODUCT INVENTORY")
print("=" * 90)

print(products)