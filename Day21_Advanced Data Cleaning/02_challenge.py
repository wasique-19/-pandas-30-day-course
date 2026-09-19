import pandas as pd
import numpy as np

# =========================================================
# 1. CREATE MESSY DATASET
# =========================================================

transactions = pd.DataFrame({
    "TransactionID": range(101, 116),

    "PaymentMethod": [
        "cc", "Credit Card", "CREDIT_CARD",
        "upi", "UPI", "Upi",
        "cash", "Cash", "CASH",
        "cc", "Credit Card", "upi",
        "Cash", "CREDIT_CARD", "UPI"
    ],

    "TransactionAmount": [
        2500, 3200, np.nan,
        1500, 1800, np.nan,
        800, 1200, 1000,
        2800, np.nan, 2000,
        900, 100000, 2200
    ]
})

print("=" * 80)
print("1. ORIGINAL MESSY DATASET")
print("=" * 80)

print(transactions)


# =========================================================
# 2. STANDARDIZE PAYMENT METHOD CATEGORIES
# =========================================================

print("\n" + "=" * 80)
print("2. PAYMENT METHOD STANDARDIZATION")
print("=" * 80)

print("Before standardization:")
print(transactions["PaymentMethod"].value_counts())

# Convert all labels to lowercase and remove spaces/underscores
transactions["PaymentMethod"] = (
    transactions["PaymentMethod"]
    .str.strip()
    .str.lower()
    .str.replace("_", " ", regex=False)
)

# Map inconsistent labels to standard categories
payment_mapping = {
    "cc": "Credit Card",
    "credit card": "Credit Card",
    "upi": "UPI",
    "cash": "Cash"
}

transactions["PaymentMethod"] = (
    transactions["PaymentMethod"]
    .map(payment_mapping)
)

print("\nAfter standardization:")
print(transactions["PaymentMethod"].value_counts())


# =========================================================
# 3. GROUP-BASED MEDIAN IMPUTATION
# Group by PaymentMethod
# Fill missing amounts with the group median
# =========================================================

print("\n" + "=" * 80)
print("3. MISSING VALUES BEFORE IMPUTATION")
print("=" * 80)

print(transactions[transactions["TransactionAmount"].isna()])


# Calculate the median amount for each payment method
group_medians = (
    transactions
    .groupby("PaymentMethod")["TransactionAmount"]
    .transform("median")
)

# Fill missing amounts using the corresponding group median
transactions["TransactionAmount"] = (
    transactions["TransactionAmount"]
    .fillna(group_medians)
)

print("\n" + "=" * 80)
print("4. DATA AFTER GROUP-BASED MEDIAN IMPUTATION")
print("=" * 80)

print(transactions)


# =========================================================
# 5. IQR-BASED OUTLIER DETECTION
# =========================================================

print("\n" + "=" * 80)
print("5. IQR OUTLIER DETECTION")
print("=" * 80)

Q1 = transactions["TransactionAmount"].quantile(0.25)
Q3 = transactions["TransactionAmount"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Identify values outside the IQR boundaries
outlier_mask = (
    (transactions["TransactionAmount"] < lower_bound) |
    (transactions["TransactionAmount"] > upper_bound)
)

# Separate outlier report
outlier_report = transactions[outlier_mask].copy()

print("\nFlagged outliers:")
print(outlier_report)


# =========================================================
# 6. FINAL CLEANED DATASET
# Add an OutlierFlag column
# =========================================================

transactions["OutlierFlag"] = np.where(
    outlier_mask,
    "Outlier",
    "Normal"
)

print("\n" + "=" * 80)
print("7. FINAL CLEANED DATASET")
print("=" * 80)

print(transactions)


# =========================================================
# 8. FINAL OUTLIER SUMMARY
# =========================================================

print("\n" + "=" * 80)
print("8. FINAL OUTLIER SUMMARY")
print("=" * 80)

print("Total transactions:", len(transactions))
print("Missing amounts:", transactions["TransactionAmount"].isna().sum())
print("Total outliers:", outlier_mask.sum())

print("\nOutlier transaction details:")
print(
    transactions.loc[
        transactions["OutlierFlag"] == "Outlier",
        ["TransactionID", "PaymentMethod", "TransactionAmount", "OutlierFlag"]
    ]
)