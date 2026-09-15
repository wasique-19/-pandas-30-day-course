import pandas as pd

# Create an employee DataFrame with 8 rows
employees = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah"],
    "Department": ["IT", "Sales", "HR", "IT", "Finance", "Sales", "HR", "IT"],
    "Age": [25, 32, 28, 35, 30, 29, 40, 27],
    "Salary": [55000, 65000, 48000, 72000, 60000, 58000, 70000, 62000]
})

# 1. Using loc[]: select Name, Department, and Salary where Salary > 60000
result1 = employees.loc[
    employees["Salary"] > 60000,
    ["Name", "Department", "Salary"]
]

print("1. Salary greater than 60000:")
print(result1)

# 2. Using isin(): select employees from IT or Sales
result2 = employees[
    employees["Department"].isin(["IT", "Sales"])
]

print("\n2. Employees in IT or Sales:")
print(result2)

# 3. Equivalent query() expression for filter 2
result3 = employees.query('Department in ["IT", "Sales"]')

print("\n3. Same filter using query():")
print(result3)

# Comment: query() is often more readable for simple conditions,
# while bracket-based filtering is more flexible for complex column selections.