import pandas as pd
import numpy as np

# =========================================================
# 1. SIMULATE AND WRITE 50,000-ROW CSV
# =========================================================

np.random.seed(42)

N = 50_000

data = pd.DataFrame({
    # Required columns
    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        size=N
    ),

    "Category": np.random.choice(
        ["Electronics", "Furniture", "Clothing", "Food"],
        size=N
    ),

    "Sales": np.random.randint(
        100, 10_000, size=N
    ),

    # Irrelevant columns
    "CustomerID": np.random.randint(
        1000, 9999, size=N
    ),

    "EmployeeName": np.random.choice(
        ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
        size=N
    )
})

# Write the complete dataset to disk
data.to_csv("sales_50000.csv", index=False)

print("CSV file created:")
print("sales_50000.csv")
print("Rows:", len(data))
print("Columns:", data.shape[1])


# =========================================================
# 2. CHUNKED PROCESSING
# =========================================================

# We only need these 3 columns.
# CustomerID and EmployeeName will NOT be loaded.
useful_columns = [
    "Region",
    "Category",
    "Sales"
]

# Store each chunk's partial aggregation
partial_results = []

# Read only 10,000 rows at a time
for chunk_number, chunk in enumerate(
    pd.read_csv(
        "sales_50000.csv",

        # Read only required columns
        usecols=useful_columns,

        # Optimize data types while reading
        dtype={
            "Region": "category",
            "Category": "category",
            "Sales": "int32"
        },

        # Never load all 50,000 rows at once
        chunksize=10_000
    ),
    start=1
):

    print(
        f"Processing chunk {chunk_number}: "
        f"{chunk.shape[0]} rows"
    )

    # -----------------------------------------------------
    # Calculate Region + Category totals for this chunk
    # -----------------------------------------------------

    chunk_summary = (
        chunk
        .groupby(
            ["Region", "Category"],
            observed=True
        )["Sales"]
        .sum()
        .reset_index()
    )

    # Store partial result
    partial_results.append(chunk_summary)


# =========================================================
# 3. COMBINE ALL PARTIAL RESULTS
# =========================================================

# Combine the small summaries, NOT the original 50,000 rows
combined_summary = pd.concat(
    partial_results,
    ignore_index=True
)

# The same Region-Category combination appears
# in multiple chunks, so aggregate again.
final_summary = (
    combined_summary
    .groupby(
        ["Region", "Category"],
        as_index=False
    )["Sales"]
    .sum()
)

# Rename for clarity
final_summary = final_summary.rename(
    columns={
        "Sales": "TotalSales"
    }
)

# Sort for easier reading
final_summary = final_summary.sort_values(
    ["Region", "Category"]
).reset_index(drop=True)


# =========================================================
# 4. PRINT FINAL SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("FINAL REGION-CATEGORY SALES SUMMARY")
print("=" * 60)

print(
    final_summary.to_string(index=False)
)


# =========================================================
# 5. VALIDATION
# =========================================================

print("\n" + "=" * 60)
print("VALIDATION")
print("=" * 60)

print(
    "Total sales from original data:",
    data["Sales"].sum()
)

print(
    "Total sales from chunk processing:",
    final_summary["TotalSales"].sum()
)

print(
    "Results match:",
    data["Sales"].sum() ==
    final_summary["TotalSales"].sum()
)