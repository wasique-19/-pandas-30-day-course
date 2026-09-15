import pandas as pd

# ============================================================
# 1. CREATE DATAFRAME
# ============================================================

transactions = pd.DataFrame({
    "Department": [
        "IT", "IT", "IT", "IT",
        "HR", "HR", "HR", "HR",
        "Sales", "Sales", "Sales", "Sales"
    ],
    "Employee": [
        "Alice", "Bob", "Alice", "Charlie",
        "David", "Emma", "David", "Emma",
        "Frank", "Grace", "Frank", "Helen"
    ],
    "ExpenseAmount": [
        5000, 3000, 2000, 4000,
        2500, 3500, 1500, 2000,
        6000, 4500, 3000, 5500
    ]
})

print("=" * 70)
print("ORIGINAL TRANSACTIONS")
print("=" * 70)
print(transactions)


# ============================================================
# 2. GROUP BY DEPARTMENT
#    Find TOTAL and AVERAGE expense
# ============================================================

department_summary = (
    transactions
    .groupby("Department")["ExpenseAmount"]
    .agg(
        TotalExpense="sum",
        AverageExpense="mean"
    )
)

print("\n" + "=" * 70)
print("DEPARTMENT EXPENSE SUMMARY")
print("=" * 70)
print(department_summary)


# ============================================================
# 3. GROUP BY DEPARTMENT + EMPLOYEE
#    Find individual employee contributions
# ============================================================

employee_summary = (
    transactions
    .groupby(["Department", "Employee"])["ExpenseAmount"]
    .sum()
    .reset_index()
    .rename(columns={
        "ExpenseAmount": "TotalExpense"
    })
)

print("\n" + "=" * 70)
print("EMPLOYEE CONTRIBUTION WITHIN EACH DEPARTMENT")
print("=" * 70)
print(employee_summary)