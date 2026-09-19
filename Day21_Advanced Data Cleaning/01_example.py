import pandas as pd
import numpy as np

# =========================================================
# DATASET
# =========================================================

employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108, 108, 110],
    "Name": [
        "Alice", "Bob", "Charlie", "Diana", "Ethan",
        "Fiona", "Grace", "Helen", "Helen", "Ian"
    ],
    "Department": [
        "IT", "it", "Sales", "SALES", "HR",
        "Hr", "IT", "Sales", "Sales", "Finance"
    ],
    "Age": [25, 30, -5, 45, 130, 28, 35, 40, 40, 32],
    "Salary": [
        55000, np.nan, 48000, 65000, 52000,
        np.nan, 72000, 68000, 68000, 200000
    ]
})

print("=" * 80)
print("ORIGINAL DATA")
print("=" * 80)
print(employees)


# =========================================================
# 1. EASY
# FIND INCONSISTENT CATEGORY LABELS
# USING value_counts() AND MAPPING
# =========================================================

print("\n" + "=" * 80)
print("1. CATEGORY LABELS BEFORE STANDARDIZATION")
print("=" * 80)

print(employees["Department"].value_counts())

# Standardize department names
department_mapping = {
    "IT": "IT",
    "it": "IT",
    "Sales": "Sales",
    "SALES": "Sales",
    "HR": "HR",
    "Hr": "HR",
    "Finance": "Finance"
}

employees["Department"] = employees["Department"].map(
    department_mapping
)

print("\nDepartment labels after standardization:")
print(employees["Department"].value_counts())


# =========================================================
# 2. EASY
# DETECT IMPLAUSIBLE AGE VALUES
# Negative ages or ages above 120
# =========================================================

print("\n" + "=" * 80)
print("2. IMPLAUSIBLE AGE VALUES")
print("=" * 80)

invalid_age_mask = (
    (employees["Age"] < 0) |
    (employees["Age"] > 120)
)

invalid_ages = employees[invalid_age_mask]

print(invalid_ages)


# =========================================================
# 3. MEDIUM
# GROUP-BASED MEDIAN IMPUTATION
# Fill missing Salary using Department median
# =========================================================

print("\n" + "=" * 80)
print("3. SALARY BEFORE IMPUTATION")
print("=" * 80)

print(employees[["Department", "Salary"]])

# Fill missing salary with the median of its department
employees["Salary"] = (
    employees["Salary"]
    .fillna(
        employees.groupby("Department")["Salary"]
        .transform("median")
    )
)

print("\nSalary after department-based median imputation:")
print(employees[["Department", "Salary"]])


# =========================================================
# 4. MEDIUM
# IQR-BASED OUTLIER DETECTION
# Applied to Salary
#
# Q1 = 25th percentile
# Q3 = 75th percentile
# IQR = Q3 - Q1
#
# Lower Bound = Q1 - 1.5 × IQR
# Upper Bound = Q3 + 1.5 × IQR
# =========================================================

print("\n" + "=" * 80)
print("4. SALARY OUTLIERS USING IQR")
print("=" * 80)

Q1 = employees["Salary"].quantile(0.25)
Q3 = employees["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

salary_outlier_mask = (
    (employees["Salary"] < lower_bound) |
    (employees["Salary"] > upper_bound)
)

salary_outliers = employees[salary_outlier_mask]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nFlagged salary outliers:")
print(salary_outliers)


# =========================================================
# 5. CHALLENGING
# COMPLETE DATA AUDIT FUNCTION
#
# Checks:
# 1. Missing values
# 2. Duplicate rows
# 3. Category consistency
# 4. Invalid ages
# 5. IQR outliers
# =========================================================

def data_audit(df):
    print("\n" + "=" * 80)
    print("DATA AUDIT REPORT")
    print("=" * 80)

    # -----------------------------------------------------
    # A. BASIC INFORMATION
    # -----------------------------------------------------

    print("\n--- BASIC INFORMATION ---")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # -----------------------------------------------------
    # B. MISSING DATA CHECK
    # -----------------------------------------------------

    print("\n--- MISSING DATA ---")

    missing_values = df.isnull().sum()

    missing_report = missing_values[
        missing_values > 0
    ]

    if missing_report.empty:
        print("No missing values found.")
    else:
        print(missing_report)

    # -----------------------------------------------------
    # C. DUPLICATE CHECK
    # -----------------------------------------------------

    print("\n--- DUPLICATE ROWS ---")

    duplicate_count = df.duplicated().sum()

    print("Number of duplicate rows:", duplicate_count)

    if duplicate_count > 0:
        print("\nDuplicate rows:")
        print(df[df.duplicated(keep=False)])

    # -----------------------------------------------------
    # D. CATEGORY CONSISTENCY CHECK
    # -----------------------------------------------------

    print("\n--- CATEGORY CONSISTENCY ---")

    category_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in category_columns:
        print(f"\nColumn: {column}")
        print("Unique labels:")
        print(df[column].value_counts(dropna=False))

        # Detect labels that differ only by capitalization
        normalized_labels = (
            df[column]
            .dropna()
            .astype(str)
            .str.strip()
            .str.lower()
        )

        original_labels = (
            df[column]
            .dropna()
            .astype(str)
            .str.strip()
        )

        if normalized_labels.nunique() < original_labels.nunique():
            print("Warning: Possible inconsistent capitalization or spacing.")
        else:
            print("No obvious capitalization inconsistency detected.")

    # -----------------------------------------------------
    # E. INVALID AGE CHECK
    # -----------------------------------------------------

    print("\n--- INVALID AGE VALUES ---")

    if "Age" in df.columns:
        invalid_age_mask = (
            (df["Age"] < 0) |
            (df["Age"] > 120)
        )

        invalid_age_rows = df[invalid_age_mask]

        print("Invalid age count:", len(invalid_age_rows))

        if not invalid_age_rows.empty:
            print(invalid_age_rows)
    else:
        print("Age column not found.")

    # -----------------------------------------------------
    # F. IQR OUTLIER CHECK
    # Applied to all numeric columns
    # -----------------------------------------------------

    print("\n--- IQR OUTLIER CHECK ---")

    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numeric_columns:

        # Ignore columns with insufficient non-null values
        if df[column].dropna().nunique() < 4:
            print(f"{column}: Not enough values for IQR analysis.")
            continue

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outlier_mask = (
            (df[column] < lower) |
            (df[column] > upper)
        )

        outlier_rows = df[outlier_mask]

        print(f"\nColumn: {column}")
        print("Lower bound:", round(lower, 2))
        print("Upper bound:", round(upper, 2))
        print("Outlier count:", len(outlier_rows))

        if not outlier_rows.empty:
            print("Flagged rows:")
            print(outlier_rows)

    print("\n" + "=" * 80)
    print("DATA AUDIT COMPLETED")
    print("=" * 80)


# =========================================================
# RUN THE AUDIT FUNCTION
# =========================================================

data_audit(employees)