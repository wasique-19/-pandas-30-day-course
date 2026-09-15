import pandas as pd

# Create a 6-row inventory DataFrame
inventory = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"],
    "Category": ["Electronics", "Accessories", "Accessories",
                 "Electronics", "Audio", "Accessories"],
    "Quantity": [10, 50, 40, 15, 30, 25],
    "UnitPrice": [55000, 900, 1800, 15000, 3500, 2500]
})

# 1. Add TotalValue = Quantity × UnitPrice
inventory["TotalValue"] = inventory["Quantity"] * inventory["UnitPrice"]

# 2. Rename all columns with proper capitalization and spacing
inventory = inventory.rename(columns={
    "Product": "Product Name",
    "Category": "Category",
    "Quantity": "Quantity",
    "UnitPrice": "Unit Price",
    "TotalValue": "Total Value"
})

# 3. Sort by Total Value in descending order
inventory = inventory.sort_values(
    by="Total Value",
    ascending=False
).reset_index(drop=True)

# 4. Insert ID column at position 0
inventory.insert(0, "ID", range(1, len(inventory) + 1))

# 5. Print the final DataFrame
print("========== FINAL INVENTORY REPORT ==========")
print(inventory.to_string(index=False))