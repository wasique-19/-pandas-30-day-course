import pandas as pd
import numpy as np

# ============================================================
# 1. SIMULATE 100-ROW ONLINE COURSE DATASET
# ============================================================

np.random.seed(42)

n = 100

df = pd.DataFrame({
    "StudentID": np.arange(1001, 1001 + n),

    "Course Category": np.random.choice(
        ["Data Science", "Web Development", "Business",
         "Design", "Marketing"],
        size=n
    ),

    "HoursSpent": np.round(
        np.random.uniform(2, 50, n), 2
    ),

    "CompletionRate": np.round(
        np.random.uniform(40, 100, n), 2
    ),

    "Rating": np.round(
        np.random.uniform(2.5, 5.0, n), 2
    )
})

print("=" * 75)
print("ONLINE COURSE PLATFORM - EDA")
print("=" * 75)


# ============================================================
# 2. DATASET UNDERSTANDING
# ============================================================

print("\n" + "=" * 75)
print("1. DATASET UNDERSTANDING")
print("=" * 75)

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nInfo:")
df.info()

print("\nDescriptive statistics:")
print(df.describe())


# ============================================================
# 3. DATA QUALITY CHECKS
# ============================================================

print("\n" + "=" * 75)
print("2. DATA QUALITY CHECKS")
print("=" * 75)

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Duplicate StudentIDs
print("\nDuplicate StudentIDs:")
print(df["StudentID"].duplicated().sum())

# Unique course categories
print("\nCourse categories:")
print(df["Course Category"].unique())

# Number of unique values
print("\nUnique values per column:")
print(df.nunique())

# Check impossible numeric values
print("\nInvalid HoursSpent (< 0):")
print((df["HoursSpent"] < 0).sum())

print("\nInvalid CompletionRate:")
print(
    ((df["CompletionRate"] < 0) |
     (df["CompletionRate"] > 100)).sum()
)

print("\nInvalid Rating:")
print(
    ((df["Rating"] < 1) |
     (df["Rating"] > 5)).sum()
)


# ============================================================
# 4. UNIVARIATE ANALYSIS - HOURSSPENT
# ============================================================

print("\n" + "=" * 75)
print("3. UNIVARIATE ANALYSIS - HOURS SPENT")
print("=" * 75)

hours = df["HoursSpent"]

print(f"Mean       : {hours.mean():.2f}")
print(f"Median     : {hours.median():.2f}")
print(f"Minimum    : {hours.min():.2f}")
print(f"Maximum    : {hours.max():.2f}")
print(f"Std Dev    : {hours.std():.2f}")
print(f"Skewness   : {hours.skew():.2f}")

print("\nQuartiles:")
print(hours.quantile([0.25, 0.50, 0.75]))


# ============================================================
# 5. UNIVARIATE ANALYSIS - RATING
# ============================================================

print("\n" + "=" * 75)
print("4. UNIVARIATE ANALYSIS - RATING")
print("=" * 75)

rating = df["Rating"]

print(f"Mean       : {rating.mean():.2f}")
print(f"Median     : {rating.median():.2f}")
print(f"Minimum    : {rating.min():.2f}")
print(f"Maximum    : {rating.max():.2f}")
print(f"Std Dev    : {rating.std():.2f}")
print(f"Skewness   : {rating.skew():.2f}")

print("\nRating quartiles:")
print(rating.quantile([0.25, 0.50, 0.75]))


# ============================================================
# 6. BIVARIATE ANALYSIS
#    COURSE CATEGORY vs COMPLETION RATE
# ============================================================

print("\n" + "=" * 75)
print("5. BIVARIATE ANALYSIS")
print("Course Category vs Completion Rate")
print("=" * 75)

category_analysis = (
    df.groupby("Course Category")["CompletionRate"]
      .agg(
          AverageCompletion="mean",
          MedianCompletion="median",
          Students="count"
      )
      .reset_index()
)

category_analysis["AverageCompletion"] = (
    category_analysis["AverageCompletion"].round(2)
)

category_analysis["MedianCompletion"] = (
    category_analysis["MedianCompletion"].round(2)
)

print(category_analysis.to_string(index=False))


# ============================================================
# 7. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 75)
print("6. CORRELATION ANALYSIS")
print("=" * 75)

numeric_columns = [
    "HoursSpent",
    "CompletionRate",
    "Rating"
]

correlation = df[numeric_columns].corr()

print("\nCorrelation matrix:")
print(correlation.round(3))


# ============================================================
# 8. FIND STRONGEST RELATIONSHIP
# ============================================================

# Extract only unique variable pairs
upper_triangle = correlation.where(
    np.triu(
        np.ones(correlation.shape),
        k=1
    ).astype(bool)
)

correlation_pairs = (
    upper_triangle
    .stack()
    .sort_values(
        key=lambda x: abs(x),
        ascending=False
    )
)

strongest_pair = correlation_pairs.index[0]
strongest_value = correlation_pairs.iloc[0]

print("\nStrongest correlation:")
print(
    f"{strongest_pair[0]} vs {strongest_pair[1]} "
    f"= {strongest_value:.3f}"
)


# ============================================================
# 9. IDENTIFY BEST/WORST CATEGORY
# ============================================================

best_category = category_analysis.loc[
    category_analysis["AverageCompletion"].idxmax()
]

lowest_category = category_analysis.loc[
    category_analysis["AverageCompletion"].idxmin()
]


# ============================================================
# 10. THREE BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 75)
print("7. BUSINESS INSIGHTS")
print("=" * 75)

print(
    f"1. {best_category['Course Category']} has the highest "
    f"average completion rate at "
    f"{best_category['AverageCompletion']:.2f}%, suggesting "
    f"that learners in this category are completing a larger "
    f"share of their courses."
)

print(
    f"2. {lowest_category['Course Category']} has the lowest "
    f"average completion rate at "
    f"{lowest_category['AverageCompletion']:.2f}%. The platform "
    f"could investigate course length, difficulty, or learner "
    f"engagement in this category."
)

print(
    f"3. {strongest_pair[0]} and {strongest_pair[1]} have the "
    f"strongest observed correlation ({strongest_value:.3f}). "
    f"This indicates an association between the two measures, "
    f"but correlation alone does not prove that one causes the other."
)