import pandas as pd

# ============================================================
# CUSTOMER SUPPORT TICKETS
# ============================================================

print("=" * 75)
print("CUSTOMER SUPPORT TICKET ANALYSIS")
print("=" * 75)


# ============================================================
# STEP 1: CREATE RAW DATASET
# ============================================================

tickets = pd.DataFrame({
    "TicketID": [
        1001, 1002, 1003, 1004, 1005,
        1006, 1007, 1008, 1009, 1010
    ],

    "Customer": [
        "Alice", "Bob", "Charlie", "Diana", "Ethan",
        "Farah", "George", "Hina", "Ivan", "Julia"
    ],

    "CreatedDate": [
        "2025-01-05",
        "2025-01-20",
        "2025-02-15",
        "2025-04-10",
        "2025-05-18",
        "2025-07-05",
        "2025-08-22",
        "2025-10-12",
        "2025-11-03",
        "2025-12-15"
    ],

    "ResolvedDate": [
        "2025-01-08",   # 3 days
        "2025-01-25",   # 5 days
        None,           # Unresolved
        "2025-04-15",   # 5 days
        "2025-05-28",   # 10 days
        "2025-07-08",   # 3 days
        None,            # Unresolved
        "2025-10-20",   # 8 days
        "2025-11-18",   # 15 days
        None             # Unresolved
    ]
})


# ============================================================
# STEP 2: PRINT RAW DATA
# ============================================================

print("\nRAW DATA:")
print(tickets)


# ============================================================
# STEP 3: CONVERT DATE COLUMNS TO DATETIME
# ============================================================

tickets["CreatedDate"] = pd.to_datetime(
    tickets["CreatedDate"]
)

tickets["ResolvedDate"] = pd.to_datetime(
    tickets["ResolvedDate"]
)


# ============================================================
# STEP 4: CALCULATE RESOLUTION DAYS
#
# ResolvedDate - CreatedDate gives Timedelta.
# .dt.days converts it into number of days.
#
# For unresolved tickets, ResolvedDate is NaT,
# so ResolutionDays will automatically be NaN.
# ============================================================

tickets["ResolutionDays"] = (
    tickets["ResolvedDate"]
    - tickets["CreatedDate"]
).dt.days


# ============================================================
# STEP 5: EXTRACT QUARTER FROM CREATED DATE
#
# dt.quarter gives:
# Q1 -> January, February, March
# Q2 -> April, May, June
# Q3 -> July, August, September
# Q4 -> October, November, December
# ============================================================

tickets["Quarter"] = (
    "Q" + tickets["CreatedDate"].dt.quarter.astype(str)
)


# ============================================================
# STEP 6: PRINT CLEANED DATAFRAME
# ============================================================

print("\n" + "=" * 75)
print("CLEANED TICKET DATA")
print("=" * 75)

print(tickets)


# ============================================================
# STEP 7: CHECK DATA TYPES
# ============================================================

print("\n" + "=" * 75)
print("DATA TYPES")
print("=" * 75)

print(tickets.dtypes)


# ============================================================
# STEP 8: QUARTERLY AVERAGE RESOLUTION TIME
#
# groupby("Quarter")
#     -> groups tickets by quarter
#
# ["ResolutionDays"]
#     -> selects resolution-time column
#
# .mean()
#     -> calculates average
#
# NaN values from unresolved tickets are automatically
# ignored by mean().
# ============================================================

quarterly_summary = (
    tickets
    .groupby("Quarter")["ResolutionDays"]
    .mean()
    .reset_index()
)


# ============================================================
# STEP 9: RENAME SUMMARY COLUMN
# ============================================================

quarterly_summary = quarterly_summary.rename(
    columns={
        "ResolutionDays": "AverageResolutionDays"
    }
)


# ============================================================
# STEP 10: PRINT QUARTERLY SUMMARY
# ============================================================

print("\n" + "=" * 75)
print("QUARTERLY AVERAGE RESOLUTION TIME")
print("=" * 75)

print(quarterly_summary)


# ============================================================
# STEP 11: OPTIONAL - ROUND AVERAGE
# ============================================================

quarterly_summary["AverageResolutionDays"] = (
    quarterly_summary["AverageResolutionDays"].round(2)
)

print("\n" + "=" * 75)
print("FINAL QUARTERLY SUMMARY")
print("=" * 75)

print(quarterly_summary)