import pandas as pd
import numpy as np
import time

# =========================================================
# 1. VECTORİZED CALCULATION vs apply(axis=1)
# =========================================================

print("=" * 70)
print("1. VECTORIZED vs apply(axis=1)")
print("=" * 70)

# Create 50,000 rows
np.random.seed(42)

df = pd.DataFrame({
    "Price": np.random.randint(100, 5000, 50000),
    "Quantity": np.random.randint(1, 20, 50000)
})

# -------------------------
# Method 1: apply(axis=1)
# -------------------------

start = time.perf_counter()

df["Total_apply"] = df.apply(
    lambda row: row["Price"] * row["Quantity"],
    axis=1
)

apply_time = time.perf_counter() - start

# -------------------------
# Method 2: Vectorized
# -------------------------

start = time.perf_counter()

df["Total_vectorized"] = (
    df["Price"] * df["Quantity"]
)

vectorized_time = time.perf_counter() - start

print(f"apply(axis=1) time : {apply_time:.6f} seconds")
print(f"Vectorized time    : {vectorized_time:.6f} seconds")

if vectorized_time > 0:
    print(
        f"Vectorized calculation is approximately "
        f"{apply_time / vectorized_time:.2f}x faster."
    )

print("\nFirst 5 rows:")
print(df.head())


# =========================================================
# 2. MEMORY: TEXT vs CATEGORY
# =========================================================

print("\n" + "=" * 70)
print("2. MEMORY BEFORE AND AFTER CATEGORY")
print("=" * 70)

customers = pd.DataFrame({
    "CustomerID": range(1, 50001),
    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        50000
    )
})

# Memory before category conversion
memory_before = customers["Region"].memory_usage(
    deep=True
)

print("Region dtype before:", customers["Region"].dtype)
print("Memory before:", memory_before, "bytes")

# Convert repeated text to category
customers["Region"] = customers["Region"].astype("category")

# Memory after category conversion
memory_after = customers["Region"].memory_usage(
    deep=True
)

print("Region dtype after :", customers["Region"].dtype)
print("Memory after :", memory_after, "bytes")

print(
    f"Memory saved: "
    f"{memory_before - memory_after:,} bytes"
)


# =========================================================
# 3. DOWNCAST NUMERIC COLUMN
# =========================================================

print("\n" + "=" * 70)
print("3. NUMERIC DOWNCASTING")
print("=" * 70)

numbers = pd.DataFrame({
    "Quantity": np.random.randint(0, 100, 100000)
})

memory_before = numbers["Quantity"].memory_usage(
    deep=True
)

print("Original dtype:", numbers["Quantity"].dtype)
print("Memory before:", memory_before, "bytes")

# Downcast to the smallest suitable integer dtype
numbers["Quantity"] = pd.to_numeric(
    numbers["Quantity"],
    downcast="integer"
)

memory_after = numbers["Quantity"].memory_usage(
    deep=True
)

print("Downcast dtype:", numbers["Quantity"].dtype)
print("Memory after:", memory_after, "bytes")

print(
    f"Memory saved: "
    f"{memory_before - memory_after:,} bytes"
)

print(
    f"Percentage saved: "
    f"{((memory_before - memory_after) / memory_before) * 100:.2f}%"
)


# =========================================================
# 4. iterrows() vs VECTORIZED VERSION
# =========================================================

print("\n" + "=" * 70)
print("4. REPLACE iterrows() WITH VECTORIZED CODE")
print("=" * 70)

sales = pd.DataFrame({
    "Price": [100, 250, 500, 1000, 200],
    "Quantity": [2, 4, 3, 5, 10]
})

# -------------------------
# OLD APPROACH: iterrows()
# -------------------------

old_results = []

for index, row in sales.iterrows():

    total = row["Price"] * row["Quantity"]

    old_results.append(total)

sales["Total_old"] = old_results

# -------------------------
# NEW APPROACH: vectorized
# -------------------------

sales["Total_vectorized"] = (
    sales["Price"] * sales["Quantity"]
)

print(sales)

print(
    "\nBoth approaches produce the same result:",
    sales["Total_old"].equals(
        sales["Total_vectorized"]
    )
)

print("""
Why vectorized code is better:
- No Python-level row loop
- No iterrows()
- Simpler code
- Usually much faster on large DataFrames
""")


# =========================================================
# 5. CHALLENGING:
# FULL OPTIMIZATION PASS
# =========================================================

print("\n" + "=" * 70)
print("5. FULL OPTIMIZATION ON 500,000+ ROWS")
print("=" * 70)

np.random.seed(42)

N = 500_000

# ---------------------------------------------------------
# CREATE LARGE DATASET
# ---------------------------------------------------------

large_df = pd.DataFrame({
    "CustomerID": np.random.randint(1, 50001, N),

    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        N
    ),

    "Category": np.random.choice(
        ["Electronics", "Furniture", "Clothing", "Food"],
        N
    ),

    "Quantity": np.random.randint(
        1, 20, N
    ),

    "Price": np.random.uniform(
        10, 5000, N
    )
})

# ---------------------------------------------------------
# BEFORE OPTIMIZATION
# ---------------------------------------------------------

memory_before = large_df.memory_usage(
    deep=True
).sum()

print("\nBEFORE OPTIMIZATION")
print("-------------------")

print("Rows:", len(large_df))
print("Columns:", len(large_df.columns))
print("Memory:",
      f"{memory_before / 1024**2:.2f} MB")

print("\nDtypes before:")
print(large_df.dtypes)


# ---------------------------------------------------------
# OPTIMIZATION 1:
# CONVERT REPEATED TEXT TO CATEGORY
# ---------------------------------------------------------

large_df["Region"] = (
    large_df["Region"].astype("category")
)

large_df["Category"] = (
    large_df["Category"].astype("category")
)


# ---------------------------------------------------------
# OPTIMIZATION 2:
# DOWNCAST INTEGER
# ---------------------------------------------------------

large_df["CustomerID"] = pd.to_numeric(
    large_df["CustomerID"],
    downcast="integer"
)

large_df["Quantity"] = pd.to_numeric(
    large_df["Quantity"],
    downcast="integer"
)


# ---------------------------------------------------------
# OPTIMIZATION 3:
# DOWNCAST FLOAT
# ---------------------------------------------------------

large_df["Price"] = pd.to_numeric(
    large_df["Price"],
    downcast="float"
)


# ---------------------------------------------------------
# OPTIMIZATION 4:
# REPLACE apply()/LOOPS WITH VECTORIZED CALCULATION
# ---------------------------------------------------------

# Instead of:
#
# large_df.apply(
#     lambda row: row["Price"] * row["Quantity"],
#     axis=1
# )
#
# Use direct vectorized multiplication:

large_df["Revenue"] = (
    large_df["Price"] *
    large_df["Quantity"]
)


# ---------------------------------------------------------
# OPTIMIZATION 5:
# CONSOLIDATE MULTIPLE AGGREGATIONS INTO ONE agg()
# ---------------------------------------------------------

customer_summary = (
    large_df
    .groupby("CustomerID")
    .agg(
        TotalRevenue=("Revenue", "sum"),
        AverageRevenue=("Revenue", "mean"),
        TotalQuantity=("Quantity", "sum"),
        OrderCount=("Revenue", "count")
    )
    .reset_index()
)


# ---------------------------------------------------------
# AFTER OPTIMIZATION
# ---------------------------------------------------------

memory_after = large_df.memory_usage(
    deep=True
).sum()

print("\nAFTER OPTIMIZATION")
print("------------------")

print("Rows:", len(large_df))
print("Columns:", len(large_df.columns))

print(
    "Memory:",
    f"{memory_after / 1024**2:.2f} MB"
)

print("\nDtypes after:")
print(large_df.dtypes)


# ---------------------------------------------------------
# MEMORY COMPARISON
# ---------------------------------------------------------

memory_saved = memory_before - memory_after

percentage_saved = (
    memory_saved / memory_before
) * 100

print("\nMEMORY SUMMARY")
print("--------------")

print(
    f"Before : {memory_before / 1024**2:.2f} MB"
)

print(
    f"After  : {memory_after / 1024**2:.2f} MB"
)

print(
    f"Saved  : {memory_saved / 1024**2:.2f} MB"
)

print(
    f"Reduction: {percentage_saved:.2f}%"
)


# ---------------------------------------------------------
# FINAL CUSTOMER SUMMARY
# ---------------------------------------------------------

print("\nCUSTOMER SUMMARY")
print("-----------------")

print(customer_summary.head(10).to_string(index=False))

print(
    "\nNumber of customer-level rows:",
    len(customer_summary)
)