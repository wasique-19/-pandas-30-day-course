import pandas as pd

# ============================================================
# 1. TEXT PRICE -> NUMERIC USING astype(int)
# ============================================================

print("=" * 65)
print("1. CONVERT TEXT PRICE TO INTEGER")
print("=" * 65)

products = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": ["100", "200", "300"]
})

print("Before conversion:")
print(products)
print("\nData types before:")
print(products.dtypes)

# Convert Price from text/object to integer
products["Price"] = products["Price"].astype(int)

print("\nAfter conversion:")
print(products)
print("\nData types after:")
print(products.dtypes)


# ============================================================
# 2. CHECK dtypes AND IDENTIFY OBJECT COLUMNS
# ============================================================

print("\n" + "=" * 65)
print("2. CHECK DATA TYPES")
print("=" * 65)

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28],
    "City": ["Delhi", "Mumbai", "Pune"],
    "Salary": [50000, 60000, 55000]
})

print("DataFrame:")
print(data)

print("\nData types:")
print(data.dtypes)

# Select columns whose dtype is object
object_columns = data.select_dtypes(include="object").columns

print("\nColumns with object dtype:")
print(object_columns.tolist())


# ============================================================
# 3. CLEAN CURRENCY VALUES
# ============================================================

print("\n" + "=" * 65)
print("3. CLEAN CURRENCY COLUMN")
print("=" * 65)

sales = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Price": ["$1,200", "$2,500", "$800"]
})

print("Before cleaning:")
print(sales)

# Remove "$" and "," using str.replace()
sales["Price"] = (
    sales["Price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convert cleaned text to numeric
sales["Price"] = pd.to_numeric(sales["Price"])

print("\nAfter cleaning:")
print(sales)

print("\nData types:")
print(sales.dtypes)


# ============================================================
# 4. YES / NO -> BOOLEAN USING map()
# ============================================================

print("\n" + "=" * 65)
print("4. CONVERT YES/NO TO BOOLEAN")
print("=" * 65)

customers = pd.DataFrame({
    "Customer": ["Alice", "Bob", "Charlie", "Diana"],
    "Subscribed": ["Yes", "No", "Yes", "No"]
})

print("Before conversion:")
print(customers)

# Convert Yes -> True and No -> False
customers["Subscribed"] = customers["Subscribed"].map({
    "Yes": True,
    "No": False
})

print("\nAfter conversion:")
print(customers)

print("\nData types:")
print(customers.dtypes)

# astype(bool) would be wrong here because non-empty strings
# like "Yes" AND "No" are both considered True by Python.
# map() correctly assigns Yes=True and No=False.


# ============================================================
# 5. CATEGORY DTYPE AND MEMORY USAGE
# ============================================================

print("\n" + "=" * 65)
print("5. MEMORY USAGE: OBJECT VS CATEGORY")
print("=" * 65)

# Create 10,000 rows with only 5 unique regions
regions = ["North", "South", "East", "West", "Central"]

inventory = pd.DataFrame({
    "Region": [regions[i % 5] for i in range(10000)]
})

# Memory usage BEFORE converting to category
memory_before = inventory["Region"].memory_usage(deep=True)

print("Unique regions:")
print(inventory["Region"].unique())

print("\nNumber of unique regions:")
print(inventory["Region"].nunique())

print("\nMemory usage before category:")
print(memory_before, "bytes")

# Convert Region to category
inventory["Region"] = inventory["Region"].astype("category")

# Memory usage AFTER converting to category
memory_after = inventory["Region"].memory_usage(deep=True)

print("\nData type after conversion:")
print(inventory["Region"].dtype)

print("\nMemory usage after category:")
print(memory_after, "bytes")

# Calculate memory saved
memory_saved = memory_before - memory_after

print("\nMemory saved:")
print(memory_saved, "bytes")

print("\nMemory reduction:")
print(
    round((memory_saved / memory_before) * 100, 2),
    "%"
)