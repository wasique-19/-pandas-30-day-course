import pandas as pd
import numpy as np

# =========================================================
# 1. EASY: BIN AGE USING pd.cut()
# =========================================================

print("=" * 60)
print("1. AGE GROUPS USING pd.cut()")
print("=" * 60)

people = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"],
    "Age": [15, 22, 35, 48, 65, 75]
})

# Custom age groups:
# 0-17   = Teen
# 18-35  = Young Adult
# 36-100 = Senior Adult

people["AgeGroup"] = pd.cut(
    people["Age"],
    bins=[0, 17, 35, 100],
    labels=["Teen", "Young Adult", "Senior Adult"],
    include_lowest=True
)

print(people)


# =========================================================
# 2. EASY: SPLIT PRICE INTO 4 QUARTILES USING pd.qcut()
# =========================================================

print("\n" + "=" * 60)
print("2. PRICE QUARTILES USING pd.qcut()")
print("=" * 60)

products = pd.DataFrame({
    "Product": [
        "Mouse", "Keyboard", "Headphones", "Monitor",
        "Tablet", "Phone", "Laptop", "Camera"
    ],
    "Price": [500, 1000, 1500, 2000, 3000, 5000, 7000, 10000]
})

# qcut divides data into 4 approximately equal-sized groups
products["PriceQuartile"] = pd.qcut(
    products["Price"],
    q=4,
    labels=["Q1 - Low", "Q2 - Medium", "Q3 - High", "Q4 - Very High"]
)

print(products)

print("\nNumber of products in each quartile:")
print(products["PriceQuartile"].value_counts().sort_index())


# =========================================================
# 3. MEDIUM: CREATE INTERACTION FEATURE
# =========================================================

print("\n" + "=" * 60)
print("3. PRICE PER UNIT FEATURE")
print("=" * 60)

sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "TotalPrice": [1000, 2500, 1800, 4000],
    "Quantity": [10, 5, 6, 8]
})

# PricePerUnit = TotalPrice / Quantity
sales["PricePerUnit"] = (
    sales["TotalPrice"] / sales["Quantity"]
).round(2)

print(sales)


# =========================================================
# 4. MEDIUM: DAYS SINCE ORDER
# =========================================================

print("\n" + "=" * 60)
print("4. DAYS SINCE ORDER")
print("=" * 60)

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "OrderDate": [
        "2026-09-01",
        "2026-09-10",
        "2026-08-20",
        "2026-09-18"
    ],
    "OrderValue": [1500, 2200, 1800, 3000]
})

# Convert OrderDate from string to datetime
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

# Use today's date dynamically
today = pd.Timestamp.today().normalize()

# Calculate the number of days since each order
orders["DaysSinceOrder"] = (
    today - orders["OrderDate"]
).dt.days

print("Today's Date:", today.date())
print(orders)


# =========================================================
# 5. CHALLENGING: CUSTOMER-LEVEL FEATURE TABLE
# =========================================================

print("\n" + "=" * 60)
print("5. CUSTOMER-LEVEL FEATURE TABLE")
print("=" * 60)

transactions = pd.DataFrame({
    "CustomerID": [
        1, 1, 1,
        2, 2,
        3, 3, 3, 3,
        4,
        5, 5
    ],

    "OrderID": [
        1001, 1002, 1003,
        1004, 1005,
        1006, 1007, 1008, 1009,
        1010,
        1011, 1012
    ],

    "OrderDate": [
        "2026-08-01", "2026-08-15", "2026-09-10",
        "2026-07-20", "2026-09-05",
        "2026-06-10", "2026-07-15", "2026-08-20", "2026-09-01",
        "2026-08-25",
        "2026-09-12", "2026-09-18"
    ],

    "OrderValue": [
        1000, 1500, 2000,
        2500, 3000,
        500, 800, 1200, 1500,
        4000,
        700, 1300
    ]
})

# Convert OrderDate into datetime format
transactions["OrderDate"] = pd.to_datetime(
    transactions["OrderDate"]
)

print("\nOriginal Transaction Data:")
print(transactions)


# ---------------------------------------------------------
# 5.1: CUSTOMER-LEVEL AGGREGATION
# ---------------------------------------------------------

customer_features = (
    transactions
    .groupby("CustomerID")
    .agg(
        TotalOrders=("OrderID", "nunique"),
        TotalSpend=("OrderValue", "sum"),
        AverageOrderValue=("OrderValue", "mean"),
        LastOrderDate=("OrderDate", "max")
    )
    .reset_index()
)

# Round average order value
customer_features["AverageOrderValue"] = (
    customer_features["AverageOrderValue"].round(2)
)


# ---------------------------------------------------------
# 5.2: DAYS SINCE LAST ORDER
# ---------------------------------------------------------

today = pd.Timestamp.today().normalize()

customer_features["DaysSinceLastOrder"] = (
    today - customer_features["LastOrderDate"]
).dt.days


# ---------------------------------------------------------
# 5.3: FINAL CUSTOMER FEATURE TABLE
# ---------------------------------------------------------

customer_features = customer_features[
    [
        "CustomerID",
        "TotalOrders",
        "TotalSpend",
        "AverageOrderValue",
        "LastOrderDate",
        "DaysSinceLastOrder"
    ]
]

print("\nFinal Customer-Level Feature Table:")
print(customer_features)


# =========================================================
# 6. FINAL SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("FEATURE SUMMARY")
print("=" * 60)

print("""
1. pd.cut()
   - Creates custom bins using specified boundaries.

2. pd.qcut()
   - Divides values into approximately equal-sized groups.

3. Interaction Feature
   - Combines existing numeric columns.
   - Example: PricePerUnit = TotalPrice / Quantity

4. DaysSinceOrder
   - Calculates days between today's date and OrderDate.

5. Customer-Level Features
   - TotalOrders: Number of unique orders
   - TotalSpend: Sum of customer spending
   - AverageOrderValue: Mean order amount
   - LastOrderDate: Most recent order date
   - DaysSinceLastOrder: Days since the latest order
""")