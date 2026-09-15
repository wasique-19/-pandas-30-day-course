import pandas as pd

# =========================================================
# DATASET: 20 CUSTOMER ORDERS
# =========================================================

orders = pd.DataFrame({
    "Region": [
        "North", "North", "North", "North", "North", "North", "North",
        "South", "South", "South", "South", "South", "South", "South",
        "West", "West", "West", "West", "West", "West"
    ],

    "ProductCategory": [
        "Electronics", "Furniture", "Clothing", "Electronics",
        "Furniture", "Clothing", "Electronics",

        "Electronics", "Furniture", "Clothing", "Electronics",
        "Furniture", "Clothing", "Furniture",

        "Electronics", "Furniture", "Clothing", "Electronics",
        "Furniture", "Clothing"
    ],

    "CustomerSegment": [
        "Retail", "Corporate", "Retail", "Corporate",
        "Retail", "Corporate", "Retail",

        "Retail", "Corporate", "Retail", "Corporate",
        "Retail", "Corporate", "Retail",

        "Corporate", "Retail", "Corporate", "Retail",
        "Corporate", "Retail"
    ],

    "Revenue": [
        12000, 8000, 5000, 15000, 7000, 6000, 9000,
        10000, 11000, 7000, 14000, 6000, 8000, 9000,
        18000, 12000, 9000, 15000, 10000, 7000
    ]
})

print("=" * 80)
print("ORIGINAL CUSTOMER ORDERS")
print("=" * 80)
print(orders)


# =========================================================
# 1. CROSSTAB
# Order counts by Region and CustomerSegment
# margins=True adds row and column totals
# =========================================================

print("\n" + "=" * 80)
print("1. ORDER COUNT BY REGION AND CUSTOMER SEGMENT")
print("=" * 80)

order_count = pd.crosstab(
    orders["Region"],
    orders["CustomerSegment"],
    margins=True
)

print(order_count)


# =========================================================
# 2. PIVOT TABLE
# Total and Average Revenue by Region and ProductCategory
#
# values   -> Revenue
# aggfunc  -> sum and mean
# fill_value=0 -> replaces missing combinations with 0
# =========================================================

print("\n" + "=" * 80)
print("2. TOTAL AND AVERAGE REVENUE BY REGION AND CATEGORY")
print("=" * 80)

revenue_summary = pd.pivot_table(
    orders,
    index="Region",
    columns="ProductCategory",
    values="Revenue",
    aggfunc=["sum", "mean"],
    fill_value=0
)

# Flatten MultiIndex columns
revenue_summary.columns = [
    "_".join(str(x) for x in column)
    for column in revenue_summary.columns
]

# Convert Region index back into a normal column
revenue_summary = revenue_summary.reset_index()

print(revenue_summary)


# =========================================================
# 3. PERCENTAGE TABLE
# Share of each region's total revenue
# contributed by each product category
# =========================================================

print("\n" + "=" * 80)
print("3. PRODUCT CATEGORY SHARE OF REGIONAL REVENUE (%)")
print("=" * 80)

# First calculate total revenue by Region + ProductCategory
category_revenue = pd.pivot_table(
    orders,
    index="Region",
    columns="ProductCategory",
    values="Revenue",
    aggfunc="sum",
    fill_value=0
)

# Divide every category revenue by that region's total revenue
percentage_table = (
    category_revenue
    .div(category_revenue.sum(axis=1), axis=0)
    * 100
)

# Round percentages to 2 decimal places
percentage_table = percentage_table.round(2)

print(percentage_table)


# =========================================================
# OPTIONAL: PRINT REGION TOTALS
# Useful for checking the percentage calculation
# =========================================================

print("\n" + "=" * 80)
print("REGIONAL TOTAL REVENUE")
print("=" * 80)

regional_totals = orders.groupby("Region")["Revenue"].sum()

print(regional_totals)