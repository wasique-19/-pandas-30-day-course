import pandas as pd

# ============================================================
# 1. CREATE WIDE-FORMAT QUARTERLY EXPENSE DATA
# ============================================================

expenses = pd.DataFrame({
    "Department": [
        "IT",
        "HR",
        "Sales",
        "Finance"
    ],
    "Q1": [25000, 12000, 18000, 15000],
    "Q2": [28000, 14000, 20000, 16000],
    "Q3": [30000, 13000, 22000, 17000],
    "Q4": [32000, 15000, 25000, 18000]
})

print("=" * 70)
print("1. ORIGINAL WIDE-FORMAT DATA")
print("=" * 70)
print(expenses)


# ============================================================
# 2. MELT WIDE → LONG
# ============================================================

long_expenses = expenses.melt(
    id_vars="Department",
    var_name="Quarter",
    value_name="Expense"
)

print("\n" + "=" * 70)
print("2. LONG-FORMAT EXPENSE DATA")
print("=" * 70)
print(long_expenses)


# ============================================================
# 3. TOTAL EXPENSE PER DEPARTMENT USING GROUPBY
# ============================================================

department_totals = (
    long_expenses
    .groupby("Department")["Expense"]
    .sum()
    .reset_index()
    .rename(columns={"Expense": "Total"})
)

print("\n" + "=" * 70)
print("3. TOTAL EXPENSE PER DEPARTMENT")
print("=" * 70)
print(department_totals)


# ============================================================
# 4. PIVOT LONG DATA BACK TO WIDE FORMAT
# ============================================================

wide_summary = long_expenses.pivot(
    index="Department",
    columns="Quarter",
    values="Expense"
).reset_index()

wide_summary.columns.name = None


# ============================================================
# 5. ADD TOTAL COLUMN
# ============================================================

wide_summary["Total"] = wide_summary[
    ["Q1", "Q2", "Q3", "Q4"]
].sum(axis=1)


# ============================================================
# 6. PRINT FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("4. FINAL WIDE SUMMARY")
print("=" * 70)
print(wide_summary)