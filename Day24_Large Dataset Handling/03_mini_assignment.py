import pandas as pd
import numpy as np

# ============================================================
# 1. CREATE 20,000 SIMULATED ROWS
# ============================================================

np.random.seed(42)

data = pd.DataFrame({
    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        size=20_000
    ),

    "Product": np.random.choice(
        ["Laptop", "Phone", "Tablet", "Headphones"],
        size=20_000
    ),

    "Sales": np.random.randint(
        500, 10_000,
        size=20_000
    ),

    # Irrelevant columns
    "CustomerID": np.arange(10001, 30001),
    "EmployeeName": np.random.choice(
        ["Alice", "Bob", "Charlie", "David", "Emma"],
        size=20_000
    )
})

# Write the simulated data to CSV
file_name = "sales_20000.csv"
data.to_csv(file_name, index=False)

print("CSV file created successfully.")
print("Number of rows:", len(data))


# ============================================================
# 2. READ CSV IN CHUNKS
#    - usecols -> only required columns
#    - dtype   -> optimize data types
#    - chunksize=5000 -> process 5,000 rows at a time
# ============================================================

partial_results = []

for chunk in pd.read_csv(
    file_name,
    usecols=["Region", "Product", "Sales"],
    dtype={
        "Region": "category",
        "Product": "category",
        "Sales": "int32"
    },
    chunksize=5000
):

    # Calculate sales total by Region for this chunk
    chunk_summary = (
        chunk.groupby("Region", observed=True)["Sales"]
        .sum()
    )

    partial_results.append(chunk_summary)


# ============================================================
# 3. COMBINE RESULTS FROM ALL CHUNKS
# ============================================================

# Combine the small per-chunk summaries
combined = pd.concat(partial_results)

# A Region appears in multiple chunks,
# so sum them again to get the final total.
final_result = (
    combined
    .groupby(level="Region")
    .sum()
    .reset_index(name="TotalSales")
)

final_result = final_result.sort_values("Region").reset_index(drop=True)


print("\nFinal Total Sales by Region:")
print(final_result)


# ============================================================
# 4. SANITY CHECK
#    Compare with loading the complete CSV directly
# ============================================================

full_data = pd.read_csv(file_name)

direct_result = (
    full_data
    .groupby("Region")["Sales"]
    .sum()
    .reset_index(name="TotalSales")
    .sort_values("Region")
    .reset_index(drop=True)
)

print("\nDirect full-file result:")
print(direct_result)


# ============================================================
# 5. VERIFY BOTH RESULTS ARE IDENTICAL
# ============================================================

is_same = final_result.equals(direct_result)

print("\nDo chunked and direct results match?")
print(is_same)