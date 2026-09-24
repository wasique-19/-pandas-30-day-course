import os
import pandas as pd


# ============================================================
# 1. LOAD THE FIVE PROJECT TABLES
# ============================================================

project_folder = "ecommerce_capstone"

table_names = [
    "customers",
    "products",
    "orders",
    "order_items",
    "payments"
]

tables = {}

for name in table_names:
    file_path = os.path.join(
        project_folder,
        f"{name}.csv"
    )

    tables[name] = pd.read_csv(file_path)


# ============================================================
# 2. REUSABLE CLEANING FUNCTION
# ============================================================

def clean_ecommerce_tables(tables):
    """
    Clean all e-commerce project tables.

    Operations:
    1. Remove exact duplicate rows.
    2. Handle missing values.
    3. Convert date columns to datetime.
    4. Standardize categorical text.
    5. Validate Quantity and UnitPrice values.
    6. Return cleaned copies of all tables.
    """

    # Make copies so the original tables are not modified
    cleaned = {
        name: table.copy()
        for name, table in tables.items()
    }

    # --------------------------------------------------------
    # A. REMOVE DUPLICATES
    # --------------------------------------------------------

    for name, df in cleaned.items():

        before = len(df)

        df.drop_duplicates(
            inplace=True
        )

        after = len(df)

        print(
            f"{name}: removed "
            f"{before - after} duplicate row(s)"
        )


    # --------------------------------------------------------
    # B. HANDLE MISSING VALUES
    # --------------------------------------------------------

    # Numeric columns:
    # Fill missing values with median.
    numeric_columns = {
        "products": ["Price"],
        "order_items": ["Quantity"],
    }

    for table_name, columns in numeric_columns.items():

        df = cleaned[table_name]

        for column in columns:

            if df[column].isna().any():

                df[column] = df[column].fillna(
                    df[column].median()
                )


    # Categorical/text columns:
    # Fill missing values with "Unknown".
    text_columns = {
        "customers": ["CustomerName", "City"],
        "products": ["ProductName", "Category"],
        "payments": [
            "PaymentMethod",
            "PaymentStatus"
        ]
    }

    for table_name, columns in text_columns.items():

        df = cleaned[table_name]

        for column in columns:

            if df[column].isna().any():

                df[column] = df[column].fillna(
                    "Unknown"
                )


    # --------------------------------------------------------
    # C. CONVERT ALL DATE COLUMNS TO DATETIME
    # --------------------------------------------------------

    for name, df in cleaned.items():

        for column in df.columns:

            if "Date" in column:

                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce"
                )


    # --------------------------------------------------------
    # D. STANDARDIZE CATEGORICAL COLUMNS
    # --------------------------------------------------------

    # Customer City
    if "City" in cleaned["customers"].columns:

        cleaned["customers"]["City"] = (
            cleaned["customers"]["City"]
            .astype("string")
            .str.strip()
            .str.title()
        )


    # Product Category
    if "Category" in cleaned["products"].columns:

        cleaned["products"]["Category"] = (
            cleaned["products"]["Category"]
            .astype("string")
            .str.strip()
            .str.title()
        )


    # Payment Method
    if "PaymentMethod" in cleaned["payments"].columns:

        cleaned["payments"]["PaymentMethod"] = (
            cleaned["payments"]["PaymentMethod"]
            .astype("string")
            .str.strip()
            .str.title()
        )


    # Payment Status
    if "PaymentStatus" in cleaned["payments"].columns:

        cleaned["payments"]["PaymentStatus"] = (
            cleaned["payments"]["PaymentStatus"]
            .astype("string")
            .str.strip()
            .str.title()
        )


    # --------------------------------------------------------
    # E. NUMERIC VALIDATION
    # --------------------------------------------------------

    # Quantity must be positive.
    if "Quantity" in cleaned["order_items"].columns:

        assert (
            cleaned["order_items"]["Quantity"] > 0
        ).all(), (
            "Validation failed: Quantity "
            "must be greater than zero."
        )


    # UnitPrice validation.
    #
    # The current project stores product price as "Price".
    # If UnitPrice is present in another version of the
    # project, validate it as well.

    if "UnitPrice" in cleaned["order_items"].columns:

        assert (
            cleaned["order_items"]["UnitPrice"] > 0
        ).all(), (
            "Validation failed: UnitPrice "
            "must be greater than zero."
        )


    # Validate product Price as well because this project
    # uses Price instead of UnitPrice.
    if "Price" in cleaned["products"].columns:

        assert (
            cleaned["products"]["Price"] > 0
        ).all(), (
            "Validation failed: Price "
            "must be greater than zero."
        )


    return cleaned


# ============================================================
# 3. RUN THE CLEANING FUNCTION
# ============================================================

print("\n" + "=" * 70)
print("CLEANING PROJECT TABLES")
print("=" * 70)

cleaned_tables = clean_ecommerce_tables(tables)


# ============================================================
# 4. VERIFY DATE DTYPES
# ============================================================

print("\n" + "=" * 70)
print("DATE COLUMN VALIDATION")
print("=" * 70)

for name, df in cleaned_tables.items():

    date_columns = [
        column
        for column in df.columns
        if "Date" in column
    ]

    for column in date_columns:

        print(
            f"{name}.{column}: "
            f"{df[column].dtype}"
        )


# ============================================================
# 5. VERIFY NO MISSING VALUES
# ============================================================

print("\n" + "=" * 70)
print("MISSING-VALUE CHECK AFTER CLEANING")
print("=" * 70)

for name, df in cleaned_tables.items():

    missing = df.isna().sum().sum()

    print(
        f"{name}: {missing} missing value(s)"
    )


# ============================================================
# 6. PRINT CLEANED TABLES
# ============================================================

print("\n" + "=" * 70)
print("CLEANED TABLES")
print("=" * 70)

for name, df in cleaned_tables.items():

    print(f"\n{name.upper()}")
    print("-" * 50)
    print(df)