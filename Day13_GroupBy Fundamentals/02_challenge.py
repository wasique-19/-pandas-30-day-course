import pandas as pd

# ============================================================
# 1. CREATE TRANSACTIONS DATAFRAME
# ============================================================

transactions = pd.DataFrame({
    "StoreID": [
        "Store_A", "Store_A", "Store_A", "Store_A", "Store_A",
        "Store_B", "Store_B", "Store_B", "Store_B", "Store_B",
        "Store_C", "Store_C", "Store_C", "Store_C", "Store_C"
    ],

    "ProductCategory": [
        "Electronics", "Clothing", "Grocery", "Electronics", "Clothing",
        "Electronics", "Clothing", "Grocery", "Electronics", "Grocery",
        "Electronics", "Clothing", "Grocery", "Clothing", "Electronics"
    ],

    "Revenue": [
        25000, 12000, 8000, 18000, 10000,
        30000, 15000, 9000, 22000, 11000,
        20000, 14000, 13000, 16000, 35000
    ]
})

print("=" * 70)
print("ORIGINAL TRANSACTIONS")
print("=" * 70)
print(transactions)


# ============================================================
# 2. TOTAL REVENUE PER STORE
# ============================================================

revenue_per_store = (
    transactions
    .groupby("StoreID")["Revenue"]
    .sum()
)

print("\n" + "=" * 70)
print("TOTAL REVENUE PER STORE")
print("=" * 70)
print(revenue_per_store)


# ============================================================
# 3. TOTAL REVENUE PER STORE + CATEGORY
# ============================================================

store_category_revenue = (
    transactions
    .groupby(["StoreID", "ProductCategory"])["Revenue"]
    .sum()
)

print("\n" + "=" * 70)
print("TOTAL REVENUE PER STORE-CATEGORY")
print("=" * 70)
print(store_category_revenue)


# ============================================================
# 4. FIND THE TOP STORE-CATEGORY COMBINATION
# ============================================================

top_combination = store_category_revenue.idxmax()
top_revenue = store_category_revenue.max()

print("\n" + "=" * 70)
print("TOP STORE-CATEGORY COMBINATION")
print("=" * 70)

print(
    f"Top combination: {top_combination[0]} - "
    f"{top_combination[1]} with revenue of ₹{top_revenue:,}"
)