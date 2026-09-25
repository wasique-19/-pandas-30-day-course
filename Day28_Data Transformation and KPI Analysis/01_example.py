import pandas as pd
import os

# ============================================================
# DAY 28 - DATA TRANSFORMATION AND KPI ANALYSIS
# ============================================================

# Project folder
project_folder = "ecommerce_capstone"


# ============================================================
# 1. LOAD THE FIVE CLEANED TABLES
# ============================================================

customers = pd.read_csv(
    os.path.join(project_folder, "customers.csv")
)

products = pd.read_csv(
    os.path.join(project_folder, "products.csv")
)

orders = pd.read_csv(
    os.path.join(project_folder, "orders.csv")
)

order_items = pd.read_csv(
    os.path.join(project_folder, "order_items.csv")
)

payments = pd.read_csv(
    os.path.join(project_folder, "payments.csv")
)


# Convert OrderDate back to datetime
orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"]
)


# ============================================================
# 2. MERGE ALL REQUIRED TABLES
# ============================================================

full_data = (
    orders
    .merge(
        customers,
        on="CustomerID",
        how="left"
    )
    .merge(
        order_items,
        on="OrderID",
        how="left"
    )
    .merge(
        products,
        on="ProductID",
        how="left"
    )
)


# ============================================================
# 3. CREATE REVENUE
# ============================================================

full_data["Revenue"] = (
    full_data["Quantity"] *
    full_data["Price"]
)


print("=" * 70)
print("FULL MERGED DATASET")
print("=" * 70)

print("Shape:", full_data.shape)

print("\nData:")
print(full_data)


# ============================================================
# 4. TOTAL REVENUE AND UNIQUE ORDERS
# ============================================================

total_revenue = full_data["Revenue"].sum()

total_unique_orders = (
    full_data["OrderID"].nunique()
)

print("\n" + "=" * 70)
print("OVERALL KPIs")
print("=" * 70)

print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Total Unique Orders : {total_unique_orders}")


# ============================================================
# 5. AVERAGE ORDER VALUE
# ============================================================

order_totals = (
    full_data
    .groupby("OrderID")["Revenue"]
    .sum()
)

aov = order_totals.mean()

print(f"Average Order Value : ₹{aov:,.2f}")


# ============================================================
# 6. REVENUE PER CATEGORY
# ============================================================

category_revenue = (
    full_data
    .groupby("Category", as_index=False)
    .agg(
        TotalRevenue=("Revenue", "sum")
    )
    .sort_values(
        "TotalRevenue",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("REVENUE BY CATEGORY")
print("=" * 70)

print(category_revenue)


# ============================================================
# 7. CUSTOMER-LEVEL METRICS
# ============================================================

customer_metrics = (
    full_data
    .groupby(
        ["CustomerID", "CustomerName"],
        as_index=False
    )
    .agg(
        TotalSpend=("Revenue", "sum"),
        OrderCount=("OrderID", "nunique")
    )
)

customer_metrics["AOV"] = (
    customer_metrics["TotalSpend"] /
    customer_metrics["OrderCount"]
)

customer_metrics = customer_metrics.sort_values(
    "TotalSpend",
    ascending=False
)

print("\n" + "=" * 70)
print("CUSTOMER-LEVEL METRICS")
print("=" * 70)

print(customer_metrics)


# ============================================================
# 8. MONTHLY REVENUE TREND
# ============================================================

full_data["Month"] = (
    full_data["OrderDate"]
    .dt.to_period("M")
)

monthly_revenue = (
    full_data
    .groupby("Month", as_index=False)
    .agg(
        TotalRevenue=("Revenue", "sum")
    )
)

print("\n" + "=" * 70)
print("MONTHLY REVENUE TREND")
print("=" * 70)

print(monthly_revenue)


# ============================================================
# 9. BEST-PERFORMING MONTH
# ============================================================

best_month = monthly_revenue.loc[
    monthly_revenue["TotalRevenue"].idxmax()
]

print("\n" + "=" * 70)
print("BEST-PERFORMING MONTH")
print("=" * 70)

print(
    f"Best Month: {best_month['Month']} | "
    f"Revenue: ₹{best_month['TotalRevenue']:,.2f}"
)