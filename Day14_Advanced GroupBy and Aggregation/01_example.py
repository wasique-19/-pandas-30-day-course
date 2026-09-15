import pandas as pd


# ============================================================
# 1. EASY
# Use agg() to calculate SUM and MEAN of Sales by Region
# ============================================================

sales = pd.DataFrame({
    "Region": [
        "North", "North", "South", "South",
        "East", "East", "West", "West"
    ],
    "Sales": [
        10000, 15000, 8000, 12000,
        20000, 10000, 18000, 22000
    ]
})

# agg() calculates multiple functions
region_summary = (
    sales
    .groupby("Region")["Sales"]
    .agg(["sum", "mean"])
)

print("=" * 70)
print("1. SUM AND MEAN SALES BY REGION")
print("=" * 70)
print(region_summary)


# ============================================================
# 2. EASY
# Named aggregation for clean column names
# ============================================================

region_summary_named = (
    sales
    .groupby("Region")
    .agg(
        TotalSales=("Sales", "sum"),
        AverageSales=("Sales", "mean")
    )
    .reset_index()
)

print("\n" + "=" * 70)
print("2. NAMED AGGREGATION")
print("=" * 70)
print(region_summary_named)


# ============================================================
# 3. MEDIUM
# Use transform() to show department average salary
# next to each employee's individual salary
# ============================================================

employees = pd.DataFrame({
    "Employee": [
        "Alice", "Bob", "Charlie",
        "David", "Emma", "Frank"
    ],
    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "HR"
    ],
    "Salary": [
        60000, 70000, 80000,
        50000, 60000, 70000
    ]
})

# transform("mean") returns a value for EVERY original row
employees["DepartmentAvgSalary"] = (
    employees
    .groupby("Department")["Salary"]
    .transform("mean")
)

print("\n" + "=" * 70)
print("3. DEPARTMENT AVERAGE NEXT TO INDIVIDUAL SALARY")
print("=" * 70)
print(employees)


# ============================================================
# 4. MEDIUM
# Use filter() to keep only customers with
# MORE THAN 2 total orders
# ============================================================

orders = pd.DataFrame({
    "Customer": [
        "Alice", "Alice",
        "Bob",
        "Charlie", "Charlie", "Charlie",
        "David", "David", "David", "David"
    ],
    "OrderID": [
        101, 102,
        103,
        104, 105, 106,
        107, 108, 109, 110
    ]
})

# filter() keeps the complete groups satisfying the condition
customers_with_more_than_2 = (
    orders
    .groupby("Customer")
    .filter(lambda group: len(group) > 2)
)

print("\n" + "=" * 70)
print("4. CUSTOMERS WITH MORE THAN 2 ORDERS")
print("=" * 70)
print(customers_with_more_than_2)


# ============================================================
# 5. CHALLENGING
#
# 1. Rank employees within their department by Salary
# 2. Use transform() to calculate department average salary
# 3. Calculate difference from department average
#
# Positive = Above average
# Negative = Below average
# Zero     = Exactly average
# ============================================================

employees = pd.DataFrame({
    "Employee": [
        "Alice", "Bob", "Charlie",
        "David", "Emma", "Frank",
        "Grace", "Helen"
    ],
    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "HR",
        "Sales", "Sales"
    ],
    "Salary": [
        60000, 80000, 70000,
        50000, 65000, 55000,
        75000, 85000
    ]
})


# ------------------------------------------------------------
# Rank employees within each department
# ------------------------------------------------------------

employees["DepartmentSalaryRank"] = (
    employees
    .groupby("Department")["Salary"]
    .rank(
        ascending=False,
        method="min"
    )
    .astype(int)
)


# ------------------------------------------------------------
# Calculate department average salary using transform()
# ------------------------------------------------------------

employees["DepartmentAvgSalary"] = (
    employees
    .groupby("Department")["Salary"]
    .transform("mean")
)


# ------------------------------------------------------------
# Calculate difference from department average
#
# Salary - Department Average
# ------------------------------------------------------------

employees["DifferenceFromAvg"] = (
    employees["Salary"]
    - employees["DepartmentAvgSalary"]
)


# ------------------------------------------------------------
# Sort by Department and Rank
# ------------------------------------------------------------

employees = employees.sort_values(
    by=["Department", "DepartmentSalaryRank"]
).reset_index(drop=True)


print("\n" + "=" * 90)
print("5. DEPARTMENT SALARY RANKING + DIFFERENCE FROM AVERAGE")
print("=" * 90)
print(employees)