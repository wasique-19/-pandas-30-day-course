import pandas as pd

# ============================================================
# PART 1 — FOUR QUARTERLY SALES DATAFRAMES
# ============================================================

# Q1 Sales
q1 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Region": ["North", "South", "West"],
    "Revenue": [50000, 30000, 20000]
})

# Q2 Sales
q2 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Region": ["North", "South", "West"],
    "Revenue": [55000, 35000, 25000]
})

# Q3 Sales
q3 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Region": ["North", "South", "West"],
    "Revenue": [60000, 40000, 30000]
})

# Q4 Sales
q4 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Region": ["North", "South", "West"],
    "Revenue": [65000, 45000, 35000]
})


# ============================================================
# COMBINE Q1-Q4 INTO ONE ANNUAL DATASET
# ============================================================

annual_sales = pd.concat(
    [q1, q2, q3, q4],
    ignore_index=True
)

print("=" * 70)
print("ANNUAL SALES DATA")
print("=" * 70)
print(annual_sales)


# ============================================================
# PART 2 — CUSTOMER PROFILE DATA
# ============================================================

# Profile 1:
# Age is available, but some Income values are missing

profile1 = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 35, 28, 40],
    "Income": [None, None, 55000, None, 75000]
}).set_index("CustomerID")


# Profile 2:
# Income is available, but some Age values are missing

profile2 = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, None, None, 28, None],
    "Income": [50000, 60000, 55000, 45000, 75000]
}).set_index("CustomerID")


# ============================================================
# COMBINE PROFILES USING combine_first()
# ============================================================

completed_profile = profile1.combine_first(profile2)


# ============================================================
# FINAL CUSTOMER PROFILE
# ============================================================

print("\n" + "=" * 70)
print("COMPLETED CUSTOMER PROFILE")
print("=" * 70)
print(completed_profile)