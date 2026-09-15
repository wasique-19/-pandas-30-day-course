import pandas as pd

# ============================================================
# 1. EASY — CONCATENATE ROW-WISE
# Identical columns + ignore_index=True
# ============================================================

df1 = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [22, 25]
})

df2 = pd.DataFrame({
    "Name": ["Charlie", "Diana"],
    "Age": [28, 24]
})

result1 = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("=" * 60)
print("1. ROW-WISE CONCATENATION")
print("=" * 60)
print(result1)


# ============================================================
# 2. EASY — CONCATENATE COLUMN-WISE
# Both DataFrames share the same index
# ============================================================

names = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"]
}, index=[101, 102, 103])

marks = pd.DataFrame({
    "Score": [85, 92, 78]
}, index=[101, 102, 103])

result2 = pd.concat(
    [names, marks],
    axis=1
)

print("\n" + "=" * 60)
print("2. COLUMN-WISE CONCATENATION")
print("=" * 60)
print(result2)


# ============================================================
# 3. MEDIUM — MISMATCHED COLUMN NAMES
# Different column names create NaN values
# ============================================================

employees1 = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
})

employees2 = pd.DataFrame({
    "Name": ["Charlie", "Diana"],
    "Salary": [55000, 65000]
})

result3 = pd.concat(
    [employees1, employees2],
    ignore_index=True
)

print("\n" + "=" * 60)
print("3. CONCATENATION WITH MISMATCHED COLUMNS")
print("=" * 60)
print(result3)

# Because "Age" does not exist in employees2,
# those rows get NaN in Age.
#
# Because "Salary" does not exist in employees1,
# those rows get NaN in Salary.


# ============================================================
# 4. MEDIUM — combine_first()
# Complementary missing values
# ============================================================

data1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Email": ["alice@gmail.com", None, "charlie@gmail.com"],
    "Phone": [None, "9876543210", "9123456780"]
}, index=[101, 102, 103])

data2 = pd.DataFrame({
    "Name": [None, "Robert", None],
    "Email": ["alice@yahoo.com", "bob@gmail.com", None],
    "Phone": ["9000000001", None, "9999999999"]
}, index=[101, 102, 103])

result4 = data1.combine_first(data2)

print("\n" + "=" * 60)
print("4. combine_first()")
print("=" * 60)
print(result4)

# combine_first() means:
# - Keep values from data1 when available
# - Fill missing values from data2
#
# Example:
# Bob's Email is missing in data1,
# so bob@gmail.com is taken from data2.
#
# Charlie's Phone already exists in data1,
# so data2's value is NOT used.


# ============================================================
# 5. CHALLENGING — THREE MONTHLY SALES FILES
# Combine January, February and March
# ============================================================

january = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Laptop"],
    "Sales": [50000, 30000, 20000, 45000]
})

february = pd.DataFrame({
    "Product": ["Phone", "Tablet", "Laptop", "Headphones"],
    "Sales": [35000, 25000, 55000, 15000]
})

march = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "Sales": [60000, 40000, 30000, 18000]
})


# ------------------------------------------------------------
# Combine all three monthly datasets
# ------------------------------------------------------------

yearly_sales = pd.concat(
    [january, february, march],
    ignore_index=True
)

print("\n" + "=" * 60)
print("5. COMBINED MONTHLY SALES")
print("=" * 60)
print(yearly_sales)


# ------------------------------------------------------------
# Calculate total sales per product
# ------------------------------------------------------------

product_summary = (
    yearly_sales
    .groupby("Product")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

print("\n" + "=" * 60)
print("TOTAL SALES PER PRODUCT")
print("=" * 60)
print(product_summary)