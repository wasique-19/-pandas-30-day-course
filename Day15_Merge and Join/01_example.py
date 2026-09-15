import pandas as pd

# ============================================================
# 1. EASY — INNER JOIN
# Merge students and grades using StudentID
# ============================================================

students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "Diana"]
})

grades = pd.DataFrame({
    "StudentID": [101, 102, 103, 105],
    "Grade": [85, 92, 78, 88]
})

inner_merge = pd.merge(
    students,
    grades,
    on="StudentID",
    how="inner"
)

print("=" * 60)
print("1. INNER JOIN")
print("=" * 60)
print(inner_merge)


# ============================================================
# 2. EASY — LEFT JOIN
# Keep ALL students and bring matching grades
# ============================================================

left_merge = pd.merge(
    students,
    grades,
    on="StudentID",
    how="left"
)

print("\n" + "=" * 60)
print("2. LEFT JOIN")
print("=" * 60)
print(left_merge)

# StudentID 104 exists in students but NOT in grades,
# so Grade becomes NaN.


# ============================================================
# 3. MEDIUM — MERGE USING MULTIPLE KEYS
# Merge using Year AND Quarter together
# ============================================================

sales = pd.DataFrame({
    "Year": [2025, 2025, 2025, 2026],
    "Quarter": ["Q1", "Q2", "Q3", "Q1"],
    "Sales": [50000, 65000, 70000, 80000]
})

targets = pd.DataFrame({
    "Year": [2025, 2025, 2025, 2026],
    "Quarter": ["Q1", "Q2", "Q3", "Q2"],
    "Target": [45000, 60000, 75000, 85000]
})

multi_key_merge = pd.merge(
    sales,
    targets,
    on=["Year", "Quarter"],
    how="inner"
)

print("\n" + "=" * 60)
print("3. MERGE USING MULTIPLE KEYS")
print("=" * 60)
print(multi_key_merge)


# ============================================================
# 4. MEDIUM — JOIN USING INDEX
# Create two DataFrames with the same index
# ============================================================

student_info = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"]
}, index=[101, 102, 103, 104])

student_marks = pd.DataFrame({
    "Math": [85, 92, 78, 88],
    "Science": [90, 89, 82, 95]
}, index=[101, 102, 103, 104])

joined_data = student_info.join(student_marks)

print("\n" + "=" * 60)
print("4. JOIN USING INDEX")
print("=" * 60)
print(joined_data)


# ============================================================
# 5. CHALLENGING — DUPLICATE JOIN KEY
# Observe row-count inflation
# ============================================================

customers = pd.DataFrame({
    "CustomerID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"]
})

orders = pd.DataFrame({
    "CustomerID": [101, 101, 102, 103, 103],
    "OrderAmount": [5000, 7000, 3000, 8000, 4000]
})

duplicate_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="inner"
)

print("\n" + "=" * 60)
print("5. DUPLICATE KEY MERGE")
print("=" * 60)
print(duplicate_merge)

print("\nCustomers rows:", len(customers))
print("Orders rows:", len(orders))
print("Merged rows:", len(duplicate_merge))

# IMPORTANT:
# CustomerID 101 appears TWICE in orders.
# Therefore, Alice gets TWO rows after the merge.
#
# CustomerID 103 also appears TWICE in orders.
# Therefore, Charlie gets TWO rows.
#
# This is called ROW-COUNT INFLATION.
#
# The merge does not simply match one row to one row.
# It creates a row for EVERY matching combination.
#
# Example:
# Customer 101 -> 1 customer row × 2 order rows = 2 merged rows
# Customer 103 -> 1 customer row × 2 order rows = 2 merged rows
#
# Total merged rows = 2 + 1 + 2 = 5