#  Create a 20-row product DataFrame and build a report
#  showing its structure and a random sample.  

import pandas as pd

# Create a 20-row product DataFrame
products = pd.DataFrame({
    "Product": [
        "Laptop", "Phone", "Tablet", "Headphones", "Keyboard",
        "Mouse", "Monitor", "Printer", "Webcam", "Speaker",
        "Smartwatch", "Camera", "Router", "USB Drive", "Power Bank",
        "Charger", "Microphone", "Hard Drive", "SSD", "Projector"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics", "Accessories", "Accessories",
        "Accessories", "Electronics", "Electronics", "Accessories", "Electronics",
        "Wearables", "Electronics", "Networking", "Storage", "Accessories",
        "Accessories", "Audio", "Storage", "Storage", "Electronics"
    ],
    "Price": [
        55000, 30000, 22000, 3500, 1800,
        900, 15000, 12000, 2500, 4500,
        8000, 42000, 3500, 1200, 2500,
        1500, 6000, 7000, 6500, 28000
    ],
    "Quantity": [
        10, 25, 15, 40, 50,
        60, 20, 12, 35, 30,
        18, 8, 45, 70, 32,
        55, 20, 14, 16, 7
    ]
})

# -------------------------------
# REPORT
# -------------------------------

print("===== PRODUCT DATAFRAME REPORT =====")

# 1. Structure
print("\n1. STRUCTURE")
products.info()

# 2. Shape
print("\n2. SHAPE")
print("Rows and columns:", products.shape)

# 3. Column names
print("\n3. COLUMNS")
print(products.columns.tolist())

# 4. Data types
print("\n4. DATA TYPES")
print(products.dtypes)

# 5. First 5 rows
print("\n5. FIRST 5 ROWS")
print(products.head())

# 6. Last 5 rows
print("\n6. LAST 5 ROWS")
print(products.tail())

# 7. Random sample of 5 rows
print("\n7. RANDOM SAMPLE OF 5 ROWS")
print(products.sample(5))

# 8. Statistical summary
print("\n8. STATISTICAL SUMMARY")
print(products.describe())

# 9. Missing values
print("\n9. MISSING VALUES")
print(products.isnull().sum())