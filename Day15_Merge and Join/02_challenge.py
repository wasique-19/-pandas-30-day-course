import pandas as pd

# ============================================================
# 1. Create Employees DataFrame
# ============================================================

employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104, 105, 106],
    "Name": [
        "Alice", "Bob", "Charlie",
        "Diana", "Ethan", "Fiona"
    ],
    "DepartmentID": [1, 2, 3, 1, 2, 3]
})


# ============================================================
# 2. Create Departments DataFrame
# ============================================================

departments = pd.DataFrame({
    "DepartmentID": [1, 2, 3],
    "DepartmentName": [
        "IT",
        "Sales",
        "HR"
    ]
})


# ============================================================
# 3. Create Salaries DataFrame
# Employee 104 and 106 deliberately have NO salary record
# ============================================================

salaries = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 105],
    "Salary": [55000, 65000, 48000, 72000]
})


# ============================================================
# 4. Merge Employees + Departments
# LEFT JOIN keeps every employee
# ============================================================

employee_department = pd.merge(
    employees,
    departments,
    on="DepartmentID",
    how="left"
)


# ============================================================
# 5. Merge the result with Salaries
# LEFT JOIN keeps employees even without salary
# ============================================================

final_df = pd.merge(
    employee_department,
    salaries,
    on="EmployeeID",
    how="left"
)


# ============================================================
# 6. Select only the required columns
# ============================================================

final_df = final_df[
    ["Name", "DepartmentName", "Salary"]
]


# ============================================================
# 7. Print final result
# ============================================================

print("=" * 50)
print("FINAL EMPLOYEE DATA")
print("=" * 50)
print(final_df)