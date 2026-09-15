import pandas as pd

# Create DataFrame with 8 products
products = pd.DataFrame({
    "ProductName": [
        "Laptop", "Smartphone", "Tablet", "Headphones",
        "Keyboard", "Monitor", "Smartwatch", "Speaker"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics", "Accessories",
        "Accessories", "Electronics", "Wearables", "Audio"
    ],
    "Cost": [40000, 22000, 15000, 2000, 1000, 9000, 5000, 2500],
    "SellingPrice": [55000, 30000, 21000, 3500, 1800, 14000, 7500, 4000]
})

# 1. Create Profit column
products["Profit"] = products["SellingPrice"] - products["Cost"]

# 2. Create ProfitMargin column
products["ProfitMargin"] = products["Profit"] / products["SellingPrice"]

# 3. Rename columns for a report
products = products.rename(columns={
    "ProductName": "Product Name",
    "Category": "Category",
    "Cost": "Cost",
    "SellingPrice": "Selling Price",
    "Profit": "Profit",
    "ProfitMargin": "Profit Margin"
})

# 4. Sort by Profit descending first
products = products.sort_values("Profit", ascending=False)

# 5. Create ranking based on Profit
products.insert(0, "Rank", range(1, len(products) + 1))

# 6. Print the final report
print("========== PRODUCT PROFIT REPORT ==========")
print(products.to_string(index=False))