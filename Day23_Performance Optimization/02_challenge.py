import pandas as pd
import numpy as np

# =========================================================
# 1. SIMULATE 1,000,000 TRANSACTIONS
# =========================================================

np.random.seed(42)

N = 1_000_000

transactions = pd.DataFrame({
    "TransactionType": np.random.choice(
        ["Purchase", "Refund", "Transfer", "Withdrawal"],
        size=N
    ),

    "Amount": np.random.uniform(
        10, 5000, size=N
    ),

    "Timestamp": pd.date_range(
        start="2026-01-01",
        periods=N,
        freq="min"
    )
})

print("=" * 70)
print("ORIGINAL DATASET")
print("=" * 70)

print(transactions.head())
print("\nShape:", transactions.shape)
print("\nOriginal dtypes:")
print(transactions.dtypes)


# =========================================================
# 2. MEMORY USAGE BEFORE OPTIMIZATION
# =========================================================

memory_before = transactions.memory_usage(
    deep=True
).sum()

print("\nMemory Before Optimization:")
print(f"{memory_before / 1024**2:.2f} MB")


# =========================================================
# 3. OPTIMIZE DATA TYPES
# =========================================================

# Repeated text values use category dtype
transactions["TransactionType"] = (
    transactions["TransactionType"].astype("category")
)

# Amount range allows float32
transactions["Amount"] = pd.to_numeric(
    transactions["Amount"],
    downcast="float"
)

# Timestamp is already stored as datetime64[ns]
transactions["Timestamp"] = pd.to_datetime(
    transactions["Timestamp"]
)


# =========================================================
# 4. VECTORİZED FEATURE ENGINEERING
# =========================================================

# Example: calculate transaction fee using vectorized logic
# Purchase: 2% fee
# Refund: 1% fee
# Transfer: 1.5% fee
# Withdrawal: 2.5% fee

fee_rates = {
    "Purchase": 0.02,
    "Refund": 0.01,
    "Transfer": 0.015,
    "Withdrawal": 0.025
}

# Map fee rates to each transaction
transactions["FeeRate"] = (
    transactions["TransactionType"]
    .map(fee_rates)
    .astype("float32")
)

# Vectorized fee calculation
transactions["Fee"] = (
    transactions["Amount"] *
    transactions["FeeRate"]
).astype("float32")

# Vectorized net amount calculation
transactions["NetAmount"] = (
    transactions["Amount"] - transactions["Fee"]
).astype("float32")


# =========================================================
# 5. MEMORY USAGE AFTER OPTIMIZATION
# =========================================================

memory_after = transactions.memory_usage(
    deep=True
).sum()

memory_saved = memory_before - memory_after

percentage_saved = (
    memory_saved / memory_before
) * 100

print("\n" + "=" * 70)
print("MEMORY COMPARISON")
print("=" * 70)

print(f"Memory Before : {memory_before / 1024**2:.2f} MB")
print(f"Memory After  : {memory_after / 1024**2:.2f} MB")
print(f"Memory Saved  : {memory_saved / 1024**2:.2f} MB")
print(f"Reduction     : {percentage_saved:.2f}%")


# =========================================================
# 6. DISPLAY OPTIMIZED DATAFRAME
# =========================================================

print("\n" + "=" * 70)
print("OPTIMIZED DATAFRAME")
print("=" * 70)

print(transactions.head())

print("\nOptimized dtypes:")
print(transactions.dtypes)


# =========================================================
# 7. CONSOLIDATED SUMMARY USING agg()
# =========================================================

summary = (
    transactions
    .groupby("TransactionType", observed=True)
    .agg(
        TransactionCount=("Amount", "count"),
        TotalAmount=("Amount", "sum"),
        AverageAmount=("Amount", "mean"),
        MinimumAmount=("Amount", "min"),
        MaximumAmount=("Amount", "max"),
        TotalFee=("Fee", "sum"),
        TotalNetAmount=("NetAmount", "sum")
    )
    .reset_index()
)


# Round numeric summary columns
summary[
    [
        "TotalAmount",
        "AverageAmount",
        "MinimumAmount",
        "MaximumAmount",
        "TotalFee",
        "TotalNetAmount"
    ]
] = summary[
    [
        "TotalAmount",
        "AverageAmount",
        "MinimumAmount",
        "MaximumAmount",
        "TotalFee",
        "TotalNetAmount"
    ]
].round(2)


# =========================================================
# 8. PRINT FINAL SUMMARY REPORT
# =========================================================

print("\n" + "=" * 70)
print("FINAL TRANSACTION SUMMARY")
print("=" * 70)

print(summary.to_string(index=False))


# =========================================================
# 9. FINAL DATASET VALIDATION
# =========================================================

print("\n" + "=" * 70)
print("VALIDATION")
print("=" * 70)

print("Total rows:", len(transactions))
print(
    "Missing values:",
    transactions.isna().sum().sum()
)

print(
    "Transaction categories:",
    transactions["TransactionType"].cat.categories.tolist()
)

print(
    "Amount dtype:",
    transactions["Amount"].dtype
)

print(
    "Timestamp dtype:",
    transactions["Timestamp"].dtype
)