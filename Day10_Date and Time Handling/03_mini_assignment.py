import pandas as pd

# ============================================================
# ORDER DATA
# ============================================================

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108],

    "OrderDate": [
        "2025-01-05",
        "2025-02-14",
        "2025-03-22",
        "2025-04-10",
        "2025-06-18",
        "2025-07-05",
        "2025-09-12",
        "2025-11-20"
    ],

    "DeliveredDate": [
        "2025-01-08",
        "2025-02-18",
        "2025-03-27",
        "2025-04-14",
        "2025-06-23",
        "2025-07-09",
        "2025-09-17",
        "2025-11-25"
    ]
})


# ============================================================
# 1. CONVERT TEXT -> DATETIME
# ============================================================

orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"]
)

orders["DeliveredDate"] = pd.to_datetime(
    orders["DeliveredDate"]
)


# ============================================================
# 2. EXTRACT ORDER MONTH
# ============================================================

orders["OrderMonth"] = orders["OrderDate"].dt.month


# ============================================================
# 3. EXTRACT DAY NAME
# ============================================================

orders["OrderDayName"] = orders["OrderDate"].dt.day_name()


# ============================================================
# 4. CALCULATE DELIVERY DAYS
# ============================================================

orders["DeliveryDays"] = (
    orders["DeliveredDate"] - orders["OrderDate"]
).dt.days


# ============================================================
# 5. FILTER ORDERS FROM JANUARY TO JUNE
#
# .between(1, 6) means:
# 1 <= OrderMonth <= 6
# ============================================================

filtered_orders = orders[
    orders["OrderMonth"].between(1, 6)
]


# ============================================================
# 6. PRINT FINAL FILTERED DATAFRAME
# ============================================================

print("=" * 75)
print("FINAL FILTERED ORDERS (JANUARY - JUNE)")
print("=" * 75)

print(filtered_orders)