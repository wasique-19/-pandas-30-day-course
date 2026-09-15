import pandas as pd

# =========================================================
# DATASET: 15 ORDERS
# =========================================================

orders = pd.DataFrame({
    "Region": [
        "North", "North", "North", "North", "North",
        "South", "South", "South", "South", "South",
        "West", "West", "West", "West", "West"
    ],

    "PaymentMethod": [
        "Credit Card", "UPI", "Cash", "Credit Card", "UPI",
        "Cash", "Credit Card", "UPI", "Credit Card", "Cash",
        "UPI", "Credit Card", "Cash", "UPI", "Credit Card"
    ],

    "OrderValue": [
        5000, 3000, 2000, 7000, 4000,
        2500, 6000, 3500, 4500, 3000,
        8000, 5500, 2500, 4000, 7000
    ]
})


# =========================================================
# 1. CROSSTAB
# Order counts by Region and PaymentMethod
# margins=True adds row and column totals
# =========================================================

print("=" * 75)
print("1. ORDER COUNT BY REGION AND PAYMENT METHOD")
print("=" * 75)

order_counts = pd.crosstab(
    orders["Region"],
    orders["PaymentMethod"],
    margins=True
)

print(order_counts)


# =========================================================
# 2. PIVOT TABLE
# Total OrderValue by Region and PaymentMethod
#
# fill_value=0 → missing combinations become 0
# margins=True   → adds All row and column
# =========================================================

print("\n" + "=" * 75)
print("2. TOTAL ORDER VALUE BY REGION AND PAYMENT METHOD")
print("=" * 75)

value_table = pd.pivot_table(
    orders,
    index="Region",
    columns="PaymentMethod",
    values="OrderValue",
    aggfunc="sum",
    fill_value=0,
    margins=True
)

print(value_table)


# =========================================================
# 3. PERCENTAGE TABLE
# Each payment method's share within each region
#
# Formula:
# Payment Method Revenue / Region Total Revenue × 100
# =========================================================

print("\n" + "=" * 75)
print("3. PAYMENT METHOD SHARE WITHIN EACH REGION (%)")
print("=" * 75)

# Create revenue table without margins first
region_payment_value = pd.pivot_table(
    orders,
    index="Region",
    columns="PaymentMethod",
    values="OrderValue",
    aggfunc="sum",
    fill_value=0
)

# Divide each value by its region's total
percentage_table = (
    region_payment_value
    .div(region_payment_value.sum(axis=1), axis=0)
    * 100
)

percentage_table = percentage_table.round(2)

print(percentage_table)


# =========================================================
# INTERPRETATION
# =========================================================

print("\n" + "=" * 75)
print("INTERPRETATION")
print("=" * 75)

print(
    "The percentages show that Credit Card contributes the largest "
    "share of revenue in North and West, while Cash contributes the "
    "largest share in South."
)