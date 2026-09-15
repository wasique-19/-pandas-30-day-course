#Create a DataFrame containing 10 products with:

#`Product`, `Category`, `Price`, `Quantity`, `Rating`.

#Inspect it using all major methods learned today

import pandas as pd

# Create DataFrame
products = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard",
                "Mouse", "Monitor", "Printer", "Webcam", "Speaker"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories",
                 "Accessories", "Accessories", "Electronics", "Electronics",
                 "Accessories", "Electronics"],
    "Price": [55000, 30000, 22000, 3500, 1800, 900, 15000, 12000, 2500, 4500],
    "Quantity": [10, 25, 15, 40, 50, 60, 20, 12, 35, 30],
    "Rating": [4.5, 4.7, 4.3, 4.6, 4.2, 4.1, 4.8, 4.0, 4.4, 4.5]
})

# 1. Display the DataFrame
print("DATAFRAME:")
print(products)

# 2. First 5 rows
print("\nHEAD:")
print(products.head())

# 3. Last 5 rows
print("\nTAIL:")
print(products.tail())

# 4. Shape - rows and columns
print("\nSHAPE:")
print(products.shape)

# 5. Column names
print("\nCOLUMNS:")
print(products.columns)

# 6. Data types
print("\nDATA TYPES:")
print(products.dtypes)

# 7. Basic information
print("\nINFO:")
products.info()

# 8. Statistical summary
print("\nDESCRIBE:")
print(products.describe())

# 9. Check for missing values
print("\nMISSING VALUES:")
print(products.isnull().sum())

# 10. Summary of categorical columns
print("\nCATEGORY SUMMARY:")
print(products["Category"].value_counts())

# 11. Unique categories
print("\nUNIQUE CATEGORIES:")
print(products["Category"].unique())

# 12. Number of unique categories
print("\nNUMBER OF UNIQUE CATEGORIES:")
print(products["Category"].nunique())