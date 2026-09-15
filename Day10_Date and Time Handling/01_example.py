import pandas as pd

# ============================================================
# 1. EASY
# DATE STRING -> DATETIME
# ============================================================

print("=" * 75)
print("1. CONVERT DATE STRINGS TO DATETIME")
print("=" * 75)

customers = pd.DataFrame({
    "Customer": ["Alice", "Bob", "Charlie", "Diana"],
    "SignupDate": [
        "2025-01-15",
        "2025-03-20",
        "2025-06-10",
        "2025-09-25"
    ]
})

print("Before conversion:")
print(customers)

print("\nDtypes before:")
print(customers.dtypes)

# Convert string column to datetime
customers["SignupDate"] = pd.to_datetime(
    customers["SignupDate"]
)

print("\nAfter conversion:")
print(customers)

print("\nDtypes after:")
print(customers.dtypes)


# ============================================================
# 2. EASY
# EXTRACT YEAR AND MONTH
# ============================================================

print("\n" + "=" * 75)
print("2. EXTRACT YEAR AND MONTH")
print("=" * 75)

customers["SignupYear"] = customers["SignupDate"].dt.year
customers["SignupMonth"] = customers["SignupDate"].dt.month

print(customers)


# ============================================================
# 3. MEDIUM
# FILTER DATE WITHIN A SPECIFIC 3-MONTH RANGE
#
# Example:
# January 1, 2025 -> March 31, 2025
# ============================================================

print("\n" + "=" * 75)
print("3. FILTER DATA FOR 3-MONTH DATE RANGE")
print("=" * 75)

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106, 107],
    "OrderDate": [
        "2025-01-10",
        "2025-02-15",
        "2025-03-25",
        "2025-04-05",
        "2025-05-18",
        "2025-06-20",
        "2025-03-05"
    ],
    "Revenue": [
        1200,
        800,
        1500,
        2000,
        900,
        1800,
        700
    ]
})

# Convert OrderDate to datetime
orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"]
)

start_date = "2025-01-01"
end_date = "2025-03-31"

filtered_orders = orders[
    orders["OrderDate"].between(
        start_date,
        end_date
    )
]

print("Orders from January to March 2025:")
print(filtered_orders)


# ============================================================
# 4. MEDIUM
# CALCULATE DAYS BETWEEN TWO DATES
#
# SignupDate -> FirstPurchaseDate
#
# datetime subtraction gives Timedelta.
# .dt.days converts it into plain integer days.
# ============================================================

print("\n" + "=" * 75)
print("4. CALCULATE DAYS BETWEEN TWO DATES")
print("=" * 75)

customers = pd.DataFrame({
    "Customer": [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Ethan"
    ],

    "SignupDate": [
        "2025-01-01",
        "2025-02-10",
        "2025-03-05",
        "2025-04-15",
        "2025-05-20"
    ],

    "FirstPurchaseDate": [
        "2025-01-06",
        "2025-02-25",
        "2025-03-08",
        "2025-04-30",
        "2025-06-01"
    ]
})

# Convert both columns to datetime
customers["SignupDate"] = pd.to_datetime(
    customers["SignupDate"]
)

customers["FirstPurchaseDate"] = pd.to_datetime(
    customers["FirstPurchaseDate"]
)

# Calculate difference in days
customers["DaysToFirstPurchase"] = (
    customers["FirstPurchaseDate"]
    - customers["SignupDate"]
).dt.days

print(customers)

print("\nDtype of DaysToFirstPurchase:")
print(customers["DaysToFirstPurchase"].dtype)


# ============================================================
# 5. CHALLENGING
# DAY NAME + TOTAL REVENUE PER DAY
# ============================================================

print("\n" + "=" * 75)
print("5. REVENUE BY DAY OF WEEK")
print("=" * 75)

orders = pd.DataFrame({
    "OrderID": range(101, 111),

    "OrderDate": [
        "2025-01-06",  # Monday
        "2025-01-07",  # Tuesday
        "2025-01-08",  # Wednesday
        "2025-01-09",  # Thursday
        "2025-01-10",  # Friday
        "2025-01-11",  # Saturday
        "2025-01-12",  # Sunday
        "2025-01-13",  # Monday
        "2025-01-14",  # Tuesday
        "2025-01-15"   # Wednesday
    ],

    "Revenue": [
        1000,
        1500,
        900,
        1200,
        2500,
        1800,
        1100,
        1300,
        1700,
        1400
    ]
})

# Convert date to datetime
orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"]
)

# Create day name column
orders["DayName"] = orders["OrderDate"].dt.day_name()

print("Orders with DayName:")
print(orders)


# ------------------------------------------------------------
# Calculate total revenue per day of week
# ------------------------------------------------------------

revenue_by_day = (
    orders
    .groupby("DayName")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n" + "-" * 75)
print("TOTAL REVENUE BY DAY")
print("-" * 75)

print(revenue_by_day)


# ------------------------------------------------------------
# Find best-performing day
# ------------------------------------------------------------

best_day = revenue_by_day.idxmax()
best_revenue = revenue_by_day.max()

print("\n" + "-" * 75)
print("BEST-PERFORMING DAY")
print("-" * 75)

print("Best day:", best_day)
print("Total revenue:", best_revenue)