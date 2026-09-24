# ============================================================
# E-COMMERCE ANALYTICS CAPSTONE PROJECT
# ============================================================

import os
import pandas as pd
import numpy as np


# ============================================================
# 1. CREATE PROJECT FOLDER
# ============================================================

project_folder = "ecommerce_capstone"

os.makedirs(project_folder, exist_ok=True)

print("Project folder created:", project_folder)


# ============================================================
# 2. PROJECT DOCUMENTATION
# ============================================================

"""
============================================================
BUSINESS PROBLEM
============================================================

The e-commerce business stores customer, product, order,
payment, and order-item information in separate tables.
The objective of this capstone is to combine and analyze
these datasets to understand sales performance, customer
behavior, product demand, and payment activity while
maintaining high data quality.

============================================================
3 BUSINESS OBJECTIVES
============================================================

1. Analyze sales and order performance across products,
   categories, and customers.

2. Understand customer purchasing behavior and identify
   valuable customers based on their order activity.

3. Analyze payment and order trends to support better
   business and operational decisions.

============================================================
PRIMARY KEY / FOREIGN KEY RELATIONSHIPS
============================================================

1. customers
   Primary Key: CustomerID

2. products
   Primary Key: ProductID

3. orders
   Primary Key: OrderID
   Foreign Key: CustomerID -> customers.CustomerID

4. order_items
   Primary Key: OrderItemID
   Foreign Keys:
       OrderID   -> orders.OrderID
       ProductID -> products.ProductID

5. payments
   Primary Key: PaymentID
   Foreign Key: OrderID -> orders.OrderID

Relationship overview:

customers
    |
    | CustomerID
    v
orders
    |
    | OrderID
    +------------------+
    |                  |
    v                  v
order_items         payments
    |
    | ProductID
    v
products
"""


# ============================================================
# 3. SIMULATE FIVE E-COMMERCE TABLES
# ============================================================

np.random.seed(42)


# ------------------------------------------------------------
# CUSTOMERS
# ------------------------------------------------------------

customers = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104, 105, 106],
    "CustomerName": [
        "Aarav", "Priya", "Rahul",
        "Sneha", "Vikram", "Ananya"
    ],
    "City": [
        "Delhi", "Mumbai", "Pune",
        "Chennai", "Delhi", "Bangalore"
    ]
})


# ------------------------------------------------------------
# PRODUCTS
# ------------------------------------------------------------

products = pd.DataFrame({
    "ProductID": [201, 202, 203, 204, 205],
    "ProductName": [
        "Laptop", "Smartphone", "Headphones",
        "Keyboard", "Monitor"
    ],
    "Category": [
        "Electronics", "Electronics", "Accessories",
        "Accessories", "Electronics"
    ],
    "Price": [
        60000, 30000, 2500, 1500, 18000
    ]
})


# ------------------------------------------------------------
# ORDERS
# ------------------------------------------------------------

orders = pd.DataFrame({
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "CustomerID": [
        101, 102, 103, 104,
        105, 106, 101, 103
    ],
    "OrderDate": pd.to_datetime([
        "2026-01-05", "2026-01-07",
        "2026-01-10", "2026-01-12",
        "2026-01-15", "2026-01-18",
        "2026-01-20", "2026-01-22"
    ])
})


# ------------------------------------------------------------
# ORDER ITEMS
# ------------------------------------------------------------

order_items = pd.DataFrame({
    "OrderItemID": range(5001, 5010),

    "OrderID": [
        1001, 1001, 1002, 1003,
        1004, 1005, 1006, 1007, 1008
    ],

    "ProductID": [
        201, 203, 202, 205,
        204, 201, 203, 202, 205
    ],

    "Quantity": [
        1, 2, 1, 1,
        3, 1, 2, 1, 2
    ]
})


# ------------------------------------------------------------
# PAYMENTS
# ------------------------------------------------------------

payments = pd.DataFrame({
    "PaymentID": range(9001, 9009),

    "OrderID": [
        1001, 1002, 1003, 1004,
        1005, 1006, 1007, 1008
    ],

    "PaymentMethod": [
        "Credit Card", "UPI", "Cash", "Credit Card",
        "UPI", "Debit Card", "UPI", "Credit Card"
    ],

    "PaymentStatus": [
        "Completed", "Completed", "Completed", "Completed",
        "Completed", "Completed", "Completed", "Completed"
    ]
})


# ============================================================
# 4. STORE TABLES AS CSV FILES
# ============================================================

tables = {
    "customers": customers,
    "products": products,
    "orders": orders,
    "order_items": order_items,
    "payments": payments
}

for table_name, table in tables.items():

    file_path = os.path.join(
        project_folder,
        f"{table_name}.csv"
    )

    table.to_csv(
        file_path,
        index=False
    )

    print(
        f"Saved {table_name}.csv "
        f"-> {table.shape}"
    )


# ============================================================
# 5. LOAD THE FIVE TABLES FROM THE PROJECT FOLDER
# ============================================================

loaded_tables = {}

for table_name in tables:

    file_path = os.path.join(
        project_folder,
        f"{table_name}.csv"
    )

    loaded_tables[table_name] = pd.read_csv(
        file_path
    )


# ============================================================
# 6. FULL DATA-QUALITY LOOP
# ============================================================

print("\n" + "=" * 75)
print("FULL DATA-QUALITY REPORT")
print("=" * 75)

for name, table in loaded_tables.items():

    print("\n" + "-" * 75)
    print(f"TABLE: {name.upper()}")
    print("-" * 75)

    # Shape
    print("Shape:", table.shape)

    # Missing values
    print("\nMissing values:")
    print(table.isnull().sum())

    print(
        "Total missing values:",
        table.isnull().sum().sum()
    )

    # Duplicate rows
    duplicate_count = table.duplicated().sum()

    print(
        "\nDuplicate rows:",
        duplicate_count
    )

    # Data types
    print("\nDtypes:")
    print(table.dtypes)

    # Unique values
    print("\nUnique values:")
    print(table.nunique())


# ============================================================
# 7. PRIMARY KEY DUPLICATE CHECK
# ============================================================

primary_keys = {
    "customers": "CustomerID",
    "products": "ProductID",
    "orders": "OrderID",
    "order_items": "OrderItemID",
    "payments": "PaymentID"
}

print("\n" + "=" * 75)
print("PRIMARY KEY VALIDATION")
print("=" * 75)

for table_name, key in primary_keys.items():

    table = loaded_tables[table_name]

    duplicates = table[key].duplicated().sum()

    print(
        f"{table_name}.{key} -> "
        f"{duplicates} duplicate key(s)"
    )


# ============================================================
# 8. PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 75)
print("CAPSTONE PROJECT SUMMARY")
print("=" * 75)

print("\nProject folder:")
print(project_folder)

print("\nTables created:")

for name, table in loaded_tables.items():
    print(
        f"- {name}: "
        f"{table.shape[0]} rows x "
        f"{table.shape[1]} columns"
    )

print("\nAll five tables loaded and quality-checked successfully.")