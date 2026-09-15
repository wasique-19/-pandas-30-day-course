#  Build an employee DataFrame from a dictionary and produce a short structural report.  

import pandas as pd

# Create employee DataFrame from a dictionary
employee_data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "Salary": [45000, 60000, 55000, 65000, 58000]
}

employees = pd.DataFrame(employee_data)

# Short structural report
print("===== EMPLOYEE STRUCTURAL REPORT =====")

print("\n1. DataFrame:")
print(employees)

print("\n2. Shape:")
print(employees.shape)

print("\n3. Columns:")
print(employees.columns.tolist())

print("\n4. Data Types:")
print(employees.dtypes)

print("\n5. First 3 Rows:")
print(employees.head(3))

print("\n6. Summary:")
employees.info()