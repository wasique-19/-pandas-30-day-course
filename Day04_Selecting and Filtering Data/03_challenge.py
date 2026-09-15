import pandas as pd

# Create a DataFrame with 10 employees
employees = pd.DataFrame({
    "Name": [
        "Alice", "Bob", "Charlie", "Diana", "Ethan",
        "Fiona", "George", "Hannah", "Ivan", "Julia"
    ],
    "Department": [
        "IT", "Sales", "HR", "IT", "Sales",
        "Finance", "IT", "Sales", "HR", "IT"
    ],
    "YearsAtCompany": [5, 2, 4, 2, 6, 7, 4, 3, 5, 8],
    "Salary": [55000, 65000, 50000, 70000, 58000, 75000, 62000, 70000, 48000, 59000]
})

# Single compound filtering expression
result = employees[
    ((employees["Department"] == "IT") & (employees["YearsAtCompany"] > 3)) |
    ((employees["Department"] == "Sales") & (employees["Salary"] > 60000))
]

print(result)