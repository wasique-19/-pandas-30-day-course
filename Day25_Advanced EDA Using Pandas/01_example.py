import pandas as pd
import numpy as np

# =========================================================
# 1. CREATE SAMPLE DATASET
# =========================================================

sales = pd.DataFrame({
    "Region": [
        "North", "South", "East", "West",
        "North", "South", "East", "West",
        "North", "South", "East", "West"
    ],

    "Sales": [
        5000, 7000, 4500, 8000,
        6000, 7500, 5000, 9000,
        5500, 6500, 4800, 8500
    ],

    "Quantity": [
        50, 70, 45, 80,
        60, 75, 50, 90,
        55, 65, 48, 85
    ],

    "Discount": [
        5, 10, 3, 8,
        6, 12, 4, 7,
        5, 9, 3, 8
    ]
})

print("=" * 70)
print("DATASET")
print("=" * 70)
print(sales)


# =========================================================
# 2. FULL DATASET UNDERSTANDING
# =========================================================

print("\n" + "=" * 70)
print("1. DATASET UNDERSTANDING")
print("=" * 70)

print("\nShape:")
print(sales.shape)

print("\nInfo:")
sales.info()

print("\nDescriptive Statistics:")
print(sales.describe())


# =========================================================
# 3. UNIVARIATE STATISTICS
# =========================================================

print("\n" + "=" * 70)
print("2. UNIVARIATE ANALYSIS - SALES")
print("=" * 70)

mean_sales = sales["Sales"].mean()
median_sales = sales["Sales"].median()
skew_sales = sales["Sales"].skew()

print(f"Mean Sales   : {mean_sales:.2f}")
print(f"Median Sales : {median_sales:.2f}")
print(f"Skewness     : {skew_sales:.2f}")


# =========================================================
# 4. BIVARIATE ANALYSIS
#    Region vs Sales
# =========================================================

print("\n" + "=" * 70)
print("3. BIVARIATE ANALYSIS - REGION vs SALES")
print("=" * 70)

region_analysis = (
    sales
    .groupby("Region")["Sales"]
    .agg(
        TotalSales="sum",
        AverageSales="mean",
        NumberOfOrders="count"
    )
    .reset_index()
)

print(region_analysis)


# =========================================================
# 5. CORRELATION MATRIX
# =========================================================

print("\n" + "=" * 70)
print("4. CORRELATION MATRIX")
print("=" * 70)

numeric_columns = [
    "Sales",
    "Quantity",
    "Discount"
]

correlation_matrix = sales[numeric_columns].corr()

print(correlation_matrix)


# =========================================================
# 6. IDENTIFY STRONGEST CORRELATION
# =========================================================

# Remove self-correlations
corr_pairs = (
    correlation_matrix
    .where(
        np.triu(
            np.ones(correlation_matrix.shape),
            k=1
        ).astype(bool)
    )
    .stack()
    .sort_values(key=abs, ascending=False)
)

strongest_pair = corr_pairs.index[0]
strongest_value = corr_pairs.iloc[0]

print("\nStrongest relationship:")
print(
    f"{strongest_pair[0]} vs {strongest_pair[1]} "
    f"= {strongest_value:.3f}"
)


# =========================================================
# 7. BUSINESS INSIGHTS
# =========================================================

print("\n" + "=" * 70)
print("5. BUSINESS INSIGHTS")
print("=" * 70)

highest_region = region_analysis.loc[
    region_analysis["AverageSales"].idxmax()
]

lowest_region = region_analysis.loc[
    region_analysis["AverageSales"].idxmin()
]

print(
    f"1. {highest_region['Region']} has the highest average "
    f"sales per order at {highest_region['AverageSales']:.2f}, "
    f"suggesting stronger sales performance per transaction."
)

print(
    f"2. {lowest_region['Region']} has the lowest average "
    f"sales per order at {lowest_region['AverageSales']:.2f}, "
    f"indicating an opportunity to investigate transaction size "
    f"or product mix in that region."
)

direction = "positive" if strongest_value > 0 else "negative"

print(
    f"3. {strongest_pair[0]} and {strongest_pair[1]} show a "
    f"{direction} correlation of {strongest_value:.3f}; "
    f"this indicates that the two variables tend to move "
    f"together, although correlation alone does not establish causation."
)