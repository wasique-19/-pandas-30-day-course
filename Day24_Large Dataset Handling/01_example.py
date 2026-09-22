import pandas as pd

# =========================================================
# CREATE A SMALL PRACTICE CSV FILE
# =========================================================

data = pd.DataFrame({
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Laptop",
        "Monitor", "Mouse", "Keyboard", "Laptop",
        "Monitor", "Mouse"
    ],

    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Accessories"
    ],

    "Quantity": [2, 10, 5, 3, 4, 8, 6, 1, 2, 12],

    "Sales": [
        2000, 500, 750, 3000,
        1600, 400, 900, 1000,
        800, 600
    ]
})

data.to_csv("sales.csv", index=False)

print("Practice CSV created successfully.")

# =========================================================
# 1. EASY: READ CSV IN CHUNKS
# =========================================================

print("\n" + "=" * 60)
print("1. CSV CHUNKS")
print("=" * 60)

# chunksize=2 means Pandas reads 2 rows at a time
for chunk in pd.read_csv("sales.csv", chunksize=2):

    print("\nChunk:")
    print(chunk)

    print("Chunk shape:", chunk.shape)


# =========================================================
# 2. EASY: USE usecols
# =========================================================

print("\n" + "=" * 60)
print("2. READ ONLY TWO COLUMNS")
print("=" * 60)

selected_columns = pd.read_csv(
    "sales.csv",
    usecols=["Product", "Sales"]
)

print(selected_columns)

print("\nColumns loaded:")
print(selected_columns.columns.tolist())


# =========================================================
# 3. MEDIUM: RUNNING TOTAL ACROSS CHUNKS
# =========================================================

print("\n" + "=" * 60)
print("3. RUNNING TOTAL OF SALES")
print("=" * 60)

running_total = 0

# Read the file in chunks
for chunk in pd.read_csv(
    "sales.csv",
    chunksize=2
):

    # Calculate the total for the current chunk
    chunk_total = chunk["Sales"].sum()

    # Add it to the running total
    running_total += chunk_total

    print(
        f"Current chunk total: {chunk_total}, "
        f"Running total: {running_total}"
    )

print("\nFinal total Sales:", running_total)


# =========================================================
# 4. MEDIUM: SPECIFY dtype DURING CSV READING
# =========================================================

print("\n" + "=" * 60)
print("4. SPECIFY DTYPES WHILE READING")
print("=" * 60)

typed_data = pd.read_csv(
    "sales.csv",

    dtype={
        "Product": "string",
        "Category": "category",
        "Quantity": "int16",
        "Sales": "int32"
    }
)

print(typed_data)

print("\nResulting dtypes:")
print(typed_data.dtypes)


# =========================================================
# 5. CHALLENGING:
# chunksize + usecols + dtype
# AND PER-CATEGORY GROUPED SUM
# =========================================================

print("\n" + "=" * 60)
print("5. CHUNKED CATEGORY-WISE SALES SUMMARY")
print("=" * 60)

# Store partial results from every chunk
partial_results = []

# Read only the columns we need
for chunk in pd.read_csv(
    "sales.csv",

    chunksize=3,

    usecols=["Category", "Sales"],

    dtype={
        "Category": "category",
        "Sales": "int32"
    }
):

    print("\nProcessing chunk:")
    print(chunk)

    # Group the current chunk by Category
    chunk_summary = (
        chunk
        .groupby("Category", observed=True)["Sales"]
        .sum()
    )

    print("\nPartial summary:")
    print(chunk_summary)

    # Store the partial result
    partial_results.append(chunk_summary)


# =========================================================
# COMBINE PARTIAL RESULTS
# =========================================================

# Concatenate all chunk-level summaries
combined = pd.concat(partial_results)

# The same category may appear in multiple chunks,
# so group again and add their partial sums.
final_summary = (
    combined
    .groupby(level=0)
    .sum()
    .reset_index()
)

# Give the columns clear names
final_summary.columns = [
    "Category",
    "TotalSales"
]

# Sort from highest to lowest sales
final_summary = final_summary.sort_values(
    "TotalSales",
    ascending=False
).reset_index(drop=True)


# =========================================================
# FINAL SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("FINAL CATEGORY-WISE SALES SUMMARY")
print("=" * 60)

print(final_summary.to_string(index=False))


# =========================================================
# VALIDATION
# =========================================================

print("\n" + "=" * 60)
print("VALIDATION")
print("=" * 60)

print(
    "Total from chunk processing:",
    final_summary["TotalSales"].sum()
)

print(
    "Total from original DataFrame:",
    data["Sales"].sum()
)

print(
    "Results match:",
    final_summary["TotalSales"].sum() == data["Sales"].sum()
)