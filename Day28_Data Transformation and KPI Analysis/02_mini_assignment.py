import pandas as pd
import os

# ============================================================
# DAY 28 - CAPSTONE KPI ANALYSIS
# ============================================================

# Folder containing the five capstone CSV files
project_folder = "ecommerce_capstone"


# ============================================================
# 1. LOAD FIVE TABLES
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


# ============================================================
# 2. CONVERT DATE COLUMN
# ============================================================

orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"]
)


# ============================================================
# 3. MERGE TABLES
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
# 4. CREATE REVENUE
# ============================================================

full_data["Revenue"] = (
    full_data["Quantity"] *
    full_data["Price"]
)


# ============================================================
# 5. TOTAL REVENUE
# ============================================================

total_revenue = full_data["Revenue"].sum()


# ============================================================
# 6. TOTAL ORDERS
# ============================================================

total_orders = full_data["OrderID"].nunique()


# ============================================================
# 7. AVERAGE ORDER VALUE
# ============================================================

order_totals = (
    full_data
    .groupby("OrderID")["Revenue"]
    .sum()
)

aov = order_totals.mean()


# ============================================================
# 8. TOP 5 PRODUCTS BY REVENUE
# ============================================================

top_5_products = (
    full_data
    .groupby(
        ["ProductID", "ProductName"],
        as_index=False
    )
    .agg(
        Revenue=("Revenue", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(5)
)


# ============================================================
# 9. MONTHLY REVENUE TREND
# ============================================================

full_data["Month"] = (
    full_data["OrderDate"]
    .dt.to_period("M")
)

monthly_revenue = (
    full_data
    .groupby("Month", as_index=False)
    .agg(
        Revenue=("Revenue", "sum")
    )
    .sort_values("Month")
)


# ============================================================
# 10. PRINT RESULTS
# ============================================================

print("\n" + "=" * 70)
print("CAPSTONE BUSINESS KPI REPORT")
print("=" * 70)


print("\n1. TOTAL REVENUE")
print("-" * 70)
print(f"₹{total_revenue:,.2f}")


print("\n2. TOTAL ORDERS")
print("-" * 70)
print(total_orders)


print("\n3. AVERAGE ORDER VALUE (AOV)")
print("-" * 70)
print(f"₹{aov:,.2f}")


print("\n4. TOP 5 PRODUCTS BY REVENUE")
print("-" * 70)
print(top_5_products.to_string(index=False))


print("\n5. MONTHLY REVENUE TREND")
print("-" * 70)
print(monthly_revenue.to_string(index=False))


print("\n" + "=" * 70)
print("REPORT COMPLETE")
print("=" * 70)