import pandas as pd

# ============================================================
# DATAFRAME
# ============================================================

employees = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Department": ["IT", "Sales", "HR", "IT", "Sales"],
    "Salary": [55000, 65000, 48000, 72000, 58000],
    "Bonus": [5000, 7000, 3000, 8000, 6000]
})

print("========== ORIGINAL DATAFRAME ==========")
print(employees)


# ============================================================
# 1. ADD TOTALCOST
# ============================================================

# TotalCost = Salary + Bonus
employees["TotalCost"] = employees["Salary"] + employees["Bonus"]

print("\n========== 1. TOTALCOST ==========")
print(employees)


# ============================================================
# 2. RENAME TWO COLUMNS
# ============================================================

employees = employees.rename(columns={
    "Salary": "AnnualSalary",
    "Bonus": "AnnualBonus"
})

print("\n========== 2. RENAMED COLUMNS ==========")
print(employees)


# ============================================================
# 3. CONDITIONAL UPDATE USING LOC
# ============================================================

# Employees earning more than 60,000 are marked as "High"
employees["SalaryLevel"] = "Standard"

employees.loc[
    employees["AnnualSalary"] > 60000,
    "SalaryLevel"
] = "High"

print("\n========== 3. CONDITIONAL UPDATE ==========")
print(employees)


# ============================================================
# 4. SORT BY TWO COLUMNS
# ============================================================

# Department → ascending
# AnnualSalary → descending
sorted_employees = employees.sort_values(
    by=["Department", "AnnualSalary"],
    ascending=[True, False]
)

print("\n========== 4. SORTED DATAFRAME ==========")
print(sorted_employees)


# ============================================================
# 5. ASSIGN() — CREATE TWO NEW COLUMNS
# ============================================================

# assign() creates a NEW DataFrame.
# The original employees DataFrame is not modified.

new_employees = employees.assign(
    TotalCompensation=(
        employees["AnnualSalary"] + employees["AnnualBonus"]
    ),
    MonthlySalary=(
        employees["AnnualSalary"] / 12
    )
)

print("\n========== 5. NEW DATAFRAME USING ASSIGN() ==========")
print(new_employees)


# ============================================================
# CONFIRM ORIGINAL DATAFRAME IS UNCHANGED
# ============================================================

print("\n========== ORIGINAL DATAFRAME AFTER ASSIGN() ==========")
print(employees)

print("\nDoes original contain TotalCompensation?",
      "TotalCompensation" in employees.columns)

print("Does original contain MonthlySalary?",
      "MonthlySalary" in employees.columns)