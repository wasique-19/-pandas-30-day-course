import pandas as pd

# =========================================================
# 1. CREATE TRANSACTION DATASET
# =========================================================

transactions = pd.DataFrame({
    "CustomerID": [
        101, 101, 101,
        102, 102, 102,
        103, 103, 103,
        104, 104, 104,
        105, 105, 105,
        106, 106, 106
    ],

    "OrderDate": [
        "2026-01-05", "2026-02-10", "2026-03-15",
        "2026-01-20", "2026-04-18", "2026-06-10",
        "2026-02-01", "2026-03-22", "2026-05-12",
        "2026-01-15", "2026-02-25", "2026-06-05",
        "2026-03-10", "2026-05-15", "2026-07-10",
        "2026-02-14", "2026-04-20", "2026-06-25"
    ],

    "Amount": [
        1000, 1500, 2000,
        3000, 3500, 4000,
        500, 800, 1200,
        4500, 5000, 5500,
        700, 900, 1100,
        6000, 6500, 7000
    ]
})

# Convert OrderDate to datetime
transactions["OrderDate"] = pd.to_datetime(
    transactions["OrderDate"]
)

print("========== ORIGINAL TRANSACTIONS ==========")
print(transactions)


# =========================================================
# 2. SET FIXED REFERENCE DATE
# =========================================================

reference_date = pd.Timestamp("2026-09-20")


# =========================================================
# 3. BUILD CUSTOMER-LEVEL FEATURE TABLE
# =========================================================

customer_features = (
    transactions
    .groupby("CustomerID")
    .agg(
        TotalOrders=("OrderDate", "count"),
        TotalSpend=("Amount", "sum"),
        AverageOrderValue=("Amount", "mean"),
        FirstOrderDate=("OrderDate", "min"),
        LastOrderDate=("OrderDate", "max")
    )
    .reset_index()
)


# =========================================================
# 4. CALCULATE DAYS SINCE FIRST AND LAST ORDER
# =========================================================

customer_features["DaysSinceFirstOrder"] = (
    reference_date - customer_features["FirstOrderDate"]
).dt.days

customer_features["DaysSinceLastOrder"] = (
    reference_date - customer_features["LastOrderDate"]
).dt.days


# =========================================================
# 5. CREATE SPEND TIER USING pd.qcut()
# =========================================================

customer_features["SpendTier"] = pd.qcut(
    customer_features["TotalSpend"],
    q=3,
    labels=["Low", "Medium", "High"]
)


# =========================================================
# 6. ROUND AND SELECT FINAL COLUMNS
# =========================================================

customer_features["AverageOrderValue"] = (
    customer_features["AverageOrderValue"].round(2)
)

customer_features = customer_features[
    [
        "CustomerID",
        "TotalOrders",
        "TotalSpend",
        "AverageOrderValue",
        "FirstOrderDate",
        "LastOrderDate",
        "DaysSinceFirstOrder",
        "DaysSinceLastOrder",
        "SpendTier"
    ]
]

customer_features = customer_features.sort_values(
    by="CustomerID"
).reset_index(drop=True)


# =========================================================
# 7. PRINT FINAL FEATURE TABLE
# =========================================================

print("\n========== FINAL CUSTOMER FEATURE TABLE ==========")

print(customer_features.to_string(index=False))


# =========================================================
# 8. IDENTIFY HIGHEST-VALUE CUSTOMER
# =========================================================

highest_value_customer = customer_features.loc[
    customer_features["TotalSpend"].idxmax()
]

print("\n========== HIGHEST-VALUE SEGMENT ==========")

print(
    f"Customer {highest_value_customer['CustomerID']} "
    f"looks like the highest-value segment because they have "
    f"the highest total spend of "
    f"{highest_value_customer['TotalSpend']}."
)