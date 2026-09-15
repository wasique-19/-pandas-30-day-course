import pandas as pd

# ============================================================
# MINI ASSIGNMENT: CUSTOMER FEEDBACK CLEANING
# ============================================================

# 1. Create a DataFrame with 10 customer feedback entries
feedback = pd.DataFrame({
    "CustomerEmail": [
        "alice@gmail.com",
        "bob@gmail.com",
        "charlie@gmail.com",
        "alice@gmail.com",       # Duplicate
        "diana@gmail.com",
        "bob@gmail.com",         # Duplicate
        "ethan@gmail.com",
        "fiona@gmail.com",
        "charlie@gmail.com",     # Duplicate
        "george@gmail.com"
    ],

    "SatisfactionLevel": [
        "good",
        "Good",
        "GOOD",
        "excellent",
        "good",
        "GOOD",
        "Excellent",
        "GOOD",
        "Good",
        "good"
    ]
})

# ============================================================
# 2. BEFORE CLEANING
# ============================================================

print("=" * 60)
print("BEFORE CLEANING")
print("=" * 60)

print(feedback)

# Store original row count
before_count = len(feedback)

print("\nRows before cleaning:", before_count)


# ============================================================
# 3. STANDARDIZE SATISFACTION LEVEL
# ============================================================

# Convert all text to lowercase first.
# Example:
# good -> good
# Good -> good
# GOOD -> good

feedback["SatisfactionLevel"] = (
    feedback["SatisfactionLevel"]
    .str.strip()
    .str.lower()
)

print("\nSatisfactionLevel after standardization:")
print(feedback["SatisfactionLevel"].unique())


# ============================================================
# 4. DEDUPLICATE BY CUSTOMER EMAIL
# ============================================================

# keep="last" means the LAST entry for each email is retained.
feedback = feedback.drop_duplicates(
    subset=["CustomerEmail"],
    keep="last"
).reset_index(drop=True)


# ============================================================
# 5. AFTER CLEANING
# ============================================================

print("\n" + "=" * 60)
print("AFTER CLEANING")
print("=" * 60)

print(feedback)

# Store final row count
after_count = len(feedback)

print("\nRows before cleaning:", before_count)
print("Rows after cleaning :", after_count)


# ============================================================
# 6. CLEANED UNIQUE SATISFACTION VALUES
# ============================================================

print("\nCleaned unique SatisfactionLevel values:")
print(feedback["SatisfactionLevel"].unique())