import pandas as pd
import numpy as np

# ============================================================
# 1. CREATE FIVE CAPSTONE TABLES WITH DELIBERATE DATA ISSUES
# ============================================================

customers = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104, 105, 106, 106],
    "CustomerName": [
        "Aarav", "Priya", "Rahul", None,
        "Vikram", "Ananya", "Ananya"
    ],
    "City": [
        "delhi", " MUMBAI ", "Pune",
        "CHENNAI", None, "bengaluru", "bengaluru"
    ]
})

products = pd.DataFrame({
    "ProductID": [201, 202, 203, 204, 205, 205],
    "ProductName": [
        "Laptop", "Smartphone", "Headphones",
        "Keyboard", "Monitor", "Monitor"
    ],
    "Category": [
        "electronics", "ELECTRONICS", " Accessories ",
        "ACCESSORIES", None, None
    ],
    "Price": [
        60000, 30000, 2500, 1500, 18000, 18000
    ]
})

orders = pd.DataFrame({
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006],
    "CustomerID": [101, 102, 103, 104, 105, 106],
    "OrderDate": [
        "2026-01-05", "2026-01-07", "2026-01-10",
        "2026-01-12", "2026-01-15", "2026-01-18"
    ]
})

order_items = pd.DataFrame({
    "OrderItemID": [5001, 5002, 5003, 5004, 5005, 5006],
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006],
    "ProductID": [201, 202, 203, 204, 205, 203],
    "Quantity": [1, 2, 1, 3, 2, 1]
})

payments = pd.DataFrame({
    "PaymentID": [9001, 9002, 9003, 9004, 9005, 9006],
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006],
    "PaymentMethod": [
        "credit card", " UPI ", "UPI",
        "DEBIT CARD", None, "Credit Card"
    ],
    "PaymentStatus": [
        "completed", "Completed", "COMPLETED",
        "pending", None, "Completed"
    ]
})

tables = {
    "customers": customers,
    "products": products,
    "orders": orders,
    "order_items": order_items,
    "payments": payments
}


# ============================================================
# 2. REUSABLE CLEANING FUNCTION
# ============================================================

def clean_capstone_tables(tables):
    cleaned = {}

    for name, df in tables.items():

        # Work on a copy so original data remains unchanged
        df = df.copy()

        # --------------------------------------------
        # Remove exact duplicate rows
        # --------------------------------------------
        df = df.drop_duplicates()

        # --------------------------------------------
        # Convert date columns
        # --------------------------------------------
        for col in df.columns:
            if "Date" in col:
                df[col] = pd.to_datetime(
                    df[col],
                    errors="coerce"
                )

        # --------------------------------------------
        # Standardize text columns
        # --------------------------------------------
        text_columns = df.select_dtypes(
            include=["object", "string"]
        ).columns

        for col in text_columns:
            df[col] = (
                df[col]
                .fillna("Unknown")
                .astype(str)
                .str.strip()
                .str.title()
            )

        # --------------------------------------------
        # Numeric missing-value handling
        # --------------------------------------------
        numeric_columns = df.select_dtypes(
            include=np.number
        ).columns

        for col in numeric_columns:

            if df[col].isna().any():

                median_value = df[col].median()

                df[col] = df[col].fillna(
                    median_value
                )

        # --------------------------------------------
        # Validation
        # --------------------------------------------

        if "Quantity" in df.columns:
            assert (
                df["Quantity"] > 0
            ).all(), "Quantity contains invalid values."

        if "Price" in df.columns:
            assert (
                df["Price"] > 0
            ).all(), "Price contains invalid values."

        if "UnitPrice" in df.columns:
            assert (
                df["UnitPrice"] > 0
            ).all(), "UnitPrice contains invalid values."

        cleaned[name] = df

    return cleaned


# ============================================================
# 3. BEFORE CLEANING QUALITY REPORT
# ============================================================

print("=" * 70)
print("BEFORE CLEANING")
print("=" * 70)

for name, df in tables.items():

    print(f"\n{name.upper()}")

    print("Missing values:")
    print(df.isna().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())


# ============================================================
# 4. RUN CLEANING FUNCTION
# ============================================================

cleaned_tables = clean_capstone_tables(tables)


# ============================================================
# 5. AFTER CLEANING QUALITY REPORT
# ============================================================

print("\n" + "=" * 70)
print("AFTER CLEANING")
print("=" * 70)

for name, df in cleaned_tables.items():

    print(f"\n{name.upper()}")

    print("Missing values:")
    print(df.isna().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())


# ============================================================
# 6. BEFORE / AFTER COMPARISON FOR AT LEAST TWO TABLES
# ============================================================

print("\n" + "=" * 70)
print("BEFORE / AFTER COMPARISON")
print("=" * 70)

for name in ["customers", "products"]:

    before = tables[name]
    after = cleaned_tables[name]

    print(f"\n{name.upper()}")
    print("-" * 50)

    comparison = pd.DataFrame({
        "Before_Missing": before.isna().sum(),
        "After_Missing": after.isna().sum(),
    })

    print("\nMissing-value comparison:")
    print(comparison)

    print(
        f"\nDuplicate rows BEFORE: "
        f"{before.duplicated().sum()}"
    )

    print(
        f"Duplicate rows AFTER : "
        f"{after.duplicated().sum()}"
    )


# ============================================================
# 7. PRINT FINAL CLEANED TABLES
# ============================================================

print("\n" + "=" * 70)
print("FINAL CLEANED TABLES")
print("=" * 70)

for name, df in cleaned_tables.items():

    print(f"\n{name.upper()}")
    print("-" * 50)
    print(df)