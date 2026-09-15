import pandas as pd

customers = pd.DataFrame({
    "Name": ["wasique", "wamique", "zaheer", "akif", "hamza", "ali"],
    "CustomerID": [1, 2, 3, 4, 5, 6],
    "Age": [22, 28, 35, 45, 31, 39],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi", "Mumbai", "Chennai"],
    "TotalSpend": [5000, 15000, 12000, 20000, 8000, 25000]
})

# 1. Customers whose age is greater than 30
result = customers[customers["Age"] > 30]

print("Age greater than 30:\n", result)

# 2. First 3 rows and first 2 columns
result = customers.iloc[:3, :2]

print("\nFirst 3 rows and first 2 columns:\n", result)

# 3. Mumbai customers, showing only Name and Age
result = customers.loc[
    customers["City"] == "Mumbai",
    ["Name", "Age"]
]

print("\nData only for Mumbai customers:\n", result)

# 4. Using boolean filtering multi-conditions
result = customers[
    (customers["Age"] > 30) &
    ((customers["City"] == "Delhi") | (customers["TotalSpend"] > 20000))
]

print(result)

# 5. Equivalent using query()
result = customers.query(
    'Age > 30 and (City == "Delhi" or TotalSpend > 20000)'
)

print(result)



