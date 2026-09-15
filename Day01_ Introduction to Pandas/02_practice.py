import pandas as pd

#  Create a Series containing five product prices. 

prices = [19.99, 24.50, 35.00, 49.99, 79.95]
product_prices = pd.Series(prices, index=["Product A", "Product B", "Product C", "Product D", "Product E"])
print(product_prices) 

#  Create a DataFrame containing five employees.

employees = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "Salary": [45000, 60000, 55000, 65000, 58000]
})

print("\nDataFrame")
print(employees)

#  Find its number of rows and columns

rows, columns = employees.shape

print("\nNumber of rows:", rows)
print("\nNumber of columns:", columns)

#  Display its data types and statistical summary.

print(employees.dtypes)
print(employees.describe())

#  Create a DataFrame with at least three numeric columns and explain the `describe()` output 

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 28, 35, 32],
    "Salary": [45000, 60000, 55000, 65000, 58000],
    "Experience": [2, 5, 3, 8, 6]
})

print("\nNew DataFrame")
print(data)
print("\nStatistical Summary")
print(data.describe())