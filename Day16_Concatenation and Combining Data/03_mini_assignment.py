import pandas as pd

# ============================================================
# PART 1 — THREE WEEKLY SALES FILES
# ============================================================

# Week 1
week1 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "UnitsSold": [20, 35, 15, 25]
})

# Week 2
week2 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "UnitsSold": [25, 40, 18, 30]
})

# Week 3
week3 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "UnitsSold": [30, 45, 20, 35]
})


# ============================================================
# CONCATENATE ALL THREE WEEKS
# ============================================================

monthly_sales = pd.concat(
    [week1, week2, week3],
    ignore_index=True
)

print("=" * 60)
print("MONTHLY SALES DATA")
print("=" * 60)
print(monthly_sales)


# ============================================================
# TOTAL MONTHLY UNITS SOLD PER PRODUCT
# ============================================================

monthly_product_totals = (
    monthly_sales
    .groupby("Product")["UnitsSold"]
    .sum()
    .reset_index()
    .sort_values("UnitsSold", ascending=False)
    .reset_index(drop=True)
)

print("\n" + "=" * 60)
print("TOTAL MONTHLY UNITS SOLD")
print("=" * 60)
print(monthly_product_totals)


# ============================================================
# PART 2 — CUSTOMER PROFILES
# ============================================================

# Profile 1:
# Age is available, but Income has missing values

profile1 = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "Income": [None, 60000, None, 45000]
}).set_index("CustomerID")


# Profile 2:
# Income is available, but Age has missing values

profile2 = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, None, 35, None],
    "Income": [50000, 60000, 55000, 45000]
}).set_index("CustomerID")


# ============================================================
# COMBINE PROFILES
# ============================================================

completed_profiles = profile1.combine_first(profile2)

print("\n" + "=" * 60)
print("COMPLETED CUSTOMER PROFILES")
print("=" * 60)
print(completed_profiles)