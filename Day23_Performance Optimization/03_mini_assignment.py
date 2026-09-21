import pandas as pd
import numpy as np
import time

# =========================================================
# 1. CREATE SIMULATED DATASET (300,000 ROWS)
# =========================================================

np.random.seed(42)

N = 300_000

df = pd.DataFrame({
    "PaymentMethod": np.random.choice(
        ["UPI", "Credit Card", "Cash", "Net Banking"],
        size=N
    ),

    "Quantity": np.random.randint(
        1, 100, size=N
    ),

    "Price": np.random.uniform(
        10, 5000, size=N
    )
})

print("=" * 70)
print("ORIGINAL DATASET")
print("=" * 70)

print(df.head())
print("\nShape:", df.shape)
print("\nOriginal dtypes:")
print(df.dtypes)


# =========================================================
# 2. MEMORY USAGE BEFORE OPTIMIZATION
# =========================================================

memory_before = df.memory_usage(
    deep=True
).sum()

print("\nMemory Before Optimization:")
print(f"{memory_before / 1024**2:.2f} MB")


# =========================================================
# 3. OPTIMIZE PAYMENTMETHOD AND QUANTITY
# =========================================================

# Convert repeated text column to category
df["PaymentMethod"] = (
    df["PaymentMethod"].astype("category")
)

# Downcast Quantity to the smallest suitable integer dtype
df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    downcast="integer"
)

# Measure memory after optimization
memory_after = df.memory_usage(
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

print("\nOptimized dtypes:")
print(df.dtypes)


# =========================================================
# 4. TIME apply(axis=1) CALCULATION
# =========================================================

# Use a copy so both approaches calculate the same operation
df_apply = df.copy()

start_apply = time.perf_counter()

df_apply["Total"] = df_apply.apply(
    lambda row: row["Quantity"] * row["Price"],
    axis=1
)

apply_time = time.perf_counter() - start_apply


# =========================================================
# 5. TIME VECTORIZED CALCULATION
# =========================================================

df_vectorized = df.copy()

start_vectorized = time.perf_counter()

df_vectorized["Total"] = (
    df_vectorized["Quantity"] *
    df_vectorized["Price"]
)

vectorized_time = time.perf_counter() - start_vectorized


# =========================================================
# 6. COMPARE RUNTIMES
# =========================================================

print("\n" + "=" * 70)
print("RUNTIME COMPARISON")
print("=" * 70)

print(f"apply(axis=1) time : {apply_time:.6f} seconds")
print(f"Vectorized time    : {vectorized_time:.6f} seconds")

if vectorized_time < apply_time:
    speedup = apply_time / vectorized_time

    print(
        f"\nVectorized calculation is approximately "
        f"{speedup:.2f}x faster."
    )
else:
    print(
        "\nVectorized calculation was not faster in this run. "
        "Repeat the benchmark for more stable results."
    )


# =========================================================
# 7. VERIFY BOTH RESULTS
# =========================================================

results_match = np.allclose(
    df_apply["Total"],
    df_vectorized["Total"]
)

print("\n" + "=" * 70)
print("RESULT VALIDATION")
print("=" * 70)

print("Both calculation results match:", results_match)

print("\nFirst 5 rows:")
print(df_vectorized.head())