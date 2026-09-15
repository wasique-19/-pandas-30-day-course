import pandas as pd
import numpy as np


# ============================================================
# 1. EASY
# Rank a Score column in descending order
# Highest score = Rank 1
# ============================================================

students = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Emma", "David"],
    "Score": [75, 92, 68, 85, 92]
})

# method="min" gives the same rank to tied values
students["Rank"] = students["Score"].rank(
    ascending=False,
    method="min"
)

print("1. SCORE RANKING")
print(students)


# ============================================================
# 2. EASY
# Use nlargest() to find the top 3 rows by Revenue
# ============================================================

sales = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Revenue": [80000, 120000, 60000, 95000, 30000]
})

# Get the 3 rows with the highest Revenue
top_3 = sales.nlargest(3, "Revenue")

print("\n2. TOP 3 REVENUE")
print(top_3)


# ============================================================
# 3. MEDIUM
# Use np.where() to create PassFail
#
# Score >= 40  -> Pass
# Score < 40   -> Fail
# ============================================================

students = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Emma", "David"],
    "Score": [75, 35, 40, 28, 65]
})

# np.where(condition, value_if_true, value_if_false)
students["PassFail"] = np.where(
    students["Score"] >= 40,
    "Pass",
    "Fail"
)

print("\n3. PASS / FAIL")
print(students)


# ============================================================
# 4. MEDIUM
# Use where() to cap Price at a maximum value
#
# Maximum allowed price = 50000
# Anything above 50000 becomes 50000
# ============================================================

products = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": [45000, 75000, 30000, 60000, 5000]
})

# Keep original price when condition is True.
# If Price <= 50000 -> keep it
# If Price > 50000  -> replace with 50000
products["Price"] = products["Price"].where(
    products["Price"] <= 50000,
    50000
)

print("\n4. CAPPED PRICE")
print(products)


# ============================================================
# 5. CHALLENGING
# Use nested np.where() to create 3 Sales Tiers
#
# Sales >= 100000  -> Gold
# Sales >= 50000   -> Silver
# Sales < 50000    -> Bronze
#
# Then rank DataFrame by Sales descending
# ============================================================

sales_data = pd.DataFrame({
    "Employee": [
        "Ali", "Sara", "John", "Emma", "David", "Ayesha"
    ],
    "Sales": [
        45000, 120000, 75000, 30000, 150000, 60000
    ]
})

# Nested np.where()
#
# First condition:
# Sales >= 100000 -> Gold
#
# Otherwise check second condition:
# Sales >= 50000 -> Silver
#
# Otherwise:
# Bronze

sales_data["Tier"] = np.where(
    sales_data["Sales"] >= 100000,
    "Gold",
    np.where(
        sales_data["Sales"] >= 50000,
        "Silver",
        "Bronze"
    )
)

# Rank the DataFrame by Sales from highest to lowest
sales_data = sales_data.sort_values(
    by="Sales",
    ascending=False
).reset_index(drop=True)

print("\n5. SALES TIER + RANKING")
print(sales_data)