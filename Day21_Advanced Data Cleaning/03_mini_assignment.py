import pandas as pd
import numpy as np

# =========================================================
# 1. CREATE DATASET
# =========================================================

products = pd.DataFrame({
    "ProductID": range(101, 113),

    "ProductName": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Phone", "Charger", "Headphones", "Tablet",
        "Smartwatch", "Camera", "Speaker", "Printer"
    ],

    "Category": [
        "Electronics", "electronics", "ELECTRONICS",  # Inconsistent labels
        "Home", "home", "HOME",                       # Inconsistent labels
        "Electronics", "ELECTRONICS", "electronics",
        "Accessories", "accessories", "ACCESSORIES"
    ],

    "Price": [
        1200, 1500, np.nan,
        2200, 2500, np.nan,
        1800, 2000, 100000,  # Extreme outlier
        1300, 1600, 1900
    ],

    "Region": [
        "North", "North", "North",
        "South", "South", "South",
        "East", "East", "East",
        "West", "West", "West"
    ]
})

print("========== ORIGINAL DATASET ==========")
print(products)


# =========================================================
# 2. STANDARDIZE CATEGORY LABELS
# =========================================================

# Remove extra spaces and convert all labels to lowercase
products["Category"] = (
    products["Category"]
    .str.strip()
    .str.lower()
)

# Convert standardized labels to title case
products["Category"] = products["Category"].str.title()

print("\n========== STANDARDIZED CATEGORIES ==========")
print(products[["ProductID", "Category"]])


# =========================================================
# 3. CREATE WASMISSING FLAG
# =========================================================

# True where Price was originally missing
products["WasMissing"] = products["Price"].isna()

print("\n========== MISSING PRICE FLAG ==========")
print(products[["ProductID", "Price", "Region", "WasMissing"]])


# =========================================================
# 4. GROUP-BASED MEDIAN IMPUTATION BY REGION
# =========================================================

# Calculate the median price within each Region
region_medians = (
    products
    .groupby("Region")["Price"]
    .transform("median")
)

print("\n========== REGION MEDIANS ==========")
print(region_medians)

# Fill missing prices using the median of their Region
products["Price"] = products["Price"].fillna(region_medians)


# =========================================================
# 5. IQR-BASED OUTLIER DETECTION
# =========================================================

Q1 = products["Price"].quantile(0.25)
Q3 = products["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("\n========== IQR CALCULATION ==========")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Identify outliers
outlier_mask = (
    (products["Price"] < lower_bound) |
    (products["Price"] > upper_bound)
)

# Add outlier flag
products["OutlierFlag"] = np.where(
    outlier_mask,
    "Outlier",
    "Normal"
)


# =========================================================
# 6. FINAL CLEANED DATASET
# =========================================================

print("\n========== FINAL CLEANED DATASET ==========")
print(products)


# =========================================================
# 7. SEPARATE OUTLIER REPORT
# =========================================================

outlier_report = products[
    products["OutlierFlag"] == "Outlier"
].copy()

print("\n========== OUTLIER REPORT ==========")
print(
    outlier_report[
        [
            "ProductID",
            "ProductName",
            "Category",
            "Price",
            "Region",
            "WasMissing",
            "OutlierFlag"
        ]
    ]
)


# =========================================================
# 8. FINAL SUMMARY
# =========================================================

print("\n========== FINAL SUMMARY ==========")

print("Total Products:", len(products))
print("Missing Prices After Imputation:", products["Price"].isna().sum())
print("Originally Missing Prices:", products["WasMissing"].sum())
print("Total Outliers:", len(outlier_report))

print("\nOutlier Product IDs:")
print(outlier_report["ProductID"].tolist())