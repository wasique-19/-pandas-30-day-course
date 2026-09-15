import pandas as pd
import numpy as np


# ============================================================
# SALES DATAFRAME
# ============================================================

sales = pd.DataFrame({
    "Region": [
        "North", "South", "North", "East",
        "South", "East", "West", "West"
    ],
    "Category": [
        "Electronics", "Clothing", "Clothing", "Electronics",
        "Electronics", "Clothing", "Electronics", "Clothing"
    ],
    "Sales": [
        10000, 8000, 6000, 12000,
        9000, 7000, 15000, 5000
    ]
})

print("ORIGINAL SALES DATA")
print(sales)


# ============================================================
# 1. EASY
# Total Sales per Region
# ============================================================

total_sales = sales.groupby("Region")["Sales"].sum()

print("\n1. TOTAL SALES PER REGION")
print(total_sales)


# ============================================================
# 2. EASY
# Average Sales per Region
# ============================================================

average_sales = sales.groupby("Region")["Sales"].mean()

print("\n2. AVERAGE SALES PER REGION")
print(average_sales)


# ============================================================
# 3. MEDIUM
# Group by Region AND Category
# Calculate total Sales for each combination
# ============================================================

region_category_sales = (
    sales
    .groupby(["Region", "Category"])["Sales"]
    .sum()
)

print("\n3. SALES BY REGION AND CATEGORY")
print(region_category_sales)


# ============================================================
# 4. MEDIUM
# Compare count() and size()
# using a column containing a missing value
# ============================================================

sales_missing = pd.DataFrame({
    "Region": [
        "North", "North", "South",
        "South", "East", "East"
    ],
    "Sales": [
        10000, np.nan, 8000,
        9000, np.nan, 7000
    ]
})

print("\n4. DATA WITH MISSING VALUES")
print(sales_missing)

# count() counts NON-MISSING values
count_result = sales_missing.groupby("Region")["Sales"].count()

# size() counts ALL rows, including rows with NaN
size_result = sales_missing.groupby("Region")["Sales"].size()

print("\nCOUNT() RESULT")
print(count_result)

print("\nSIZE() RESULT")
print(size_result)


# ============================================================
# 5. CHALLENGING
# Customer Orders
#
# Calculate:
#   1. Total Spend
#   2. Order Count
#   3. Average Order Value
#
# Then reset_index() to create a flat DataFrame
# ============================================================

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108],
    "CustomerID": [1, 2, 1, 3, 2, 1, 3, 2],
    "OrderValue": [
        5000, 3000, 7000, 4000,
        6000, 2000, 8000, 5000
    ]
})

print("\nCUSTOMER ORDERS")
print(orders)

# Group by CustomerID
customer_summary = (
    orders
    .groupby("CustomerID")
    .agg(
        TotalSpend=("OrderValue", "sum"),
        OrderCount=("OrderID", "count"),
        AverageOrderValue=("OrderValue", "mean")
    )
    .reset_index()
)

# Round average values
customer_summary["AverageOrderValue"] = (
    customer_summary["AverageOrderValue"].round(2)
)

print("\n5. CUSTOMER ORDER SUMMARY")
print(customer_summary)