import pandas as pd

# ============================================================
# 1. CREATE TRANSACTION DATA
# ============================================================

sales = pd.DataFrame({
    "SalesRep": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Helen", "Ian", "Julia",
        "Kevin", "Laura", "Mike", "Nina", "Oscar"
    ],
    "Region": [
        "North", "North", "North", "North", "North",
        "South", "South", "South", "South", "South",
        "West", "West", "West", "West", "West"
    ],
    "Revenue": [
        10000, 15000, 8000, 12000, 5000,
        14000, 9000, 11000, 6000, 10000,
        20000, 15000, 10000, 12000, 18000
    ]
})


# ============================================================
# 2. BUILD REGION KPI TABLE
#
# Per region:
# - Total Revenue
# - Average Revenue per Transaction
# - Transaction Count
# ============================================================

region_kpi = (
    sales
    .groupby("Region")
    .agg(
        TotalRevenue=("Revenue", "sum"),
        AverageRevenue=("Revenue", "mean"),
        TransactionCount=("Revenue", "count")
    )
    .reset_index()
)

# Round average revenue
region_kpi["AverageRevenue"] = (
    region_kpi["AverageRevenue"].round(2)
)


# ============================================================
# 3. USE transform() ON ORIGINAL DATA
#
# Find total revenue for each transaction's region.
# transform("sum") returns the regional total
# for every individual transaction.
# ============================================================

sales["RegionTotalRevenue"] = (
    sales
    .groupby("Region")["Revenue"]
    .transform("sum")
)


# ============================================================
# 4. CALCULATE REVENUE % OF REGION TOTAL
# ============================================================

sales["RevenuePctOfRegion"] = (
    sales["Revenue"]
    / sales["RegionTotalRevenue"]
    * 100
)

# Round percentage to 2 decimal places
sales["RevenuePctOfRegion"] = (
    sales["RevenuePctOfRegion"].round(2)
)


# ============================================================
# 5. PRINT KPI TABLE
# ============================================================

print("=" * 85)
print("REGION KPI TABLE")
print("=" * 85)

print(region_kpi)


# ============================================================
# 6. PRINT ORIGINAL TRANSACTION-LEVEL DATA
# ============================================================

print("\n" + "=" * 85)
print("TRANSACTION DATA WITH % OF REGION TOTAL")
print("=" * 85)

print(sales)