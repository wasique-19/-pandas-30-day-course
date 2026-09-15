import pandas as pd

# Create an orders DataFrame
orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106],
    "OrderValue": [450, 750, 1200, 2500, 1800, 900],
    "Region": ["North", "South", "East", "North", "South", "West"]
})

# Select orders where:
# OrderValue is between 500 and 2000
# AND Region is either North or South
result = orders[
    orders["OrderValue"].between(500, 2000) &
    orders["Region"].isin(["North", "South"])
]

print(result)