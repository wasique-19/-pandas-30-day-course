import pandas as pd

# ============================================================
# 1. CREATE DATAFRAME + DATETIMEINDEX
# ============================================================

# Daily sales data for 3 months
df = pd.DataFrame({
    "date": [
        "2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04",
        "2026-01-05", "2026-01-06", "2026-01-07", "2026-01-08",
        "2026-01-09", "2026-01-10", "2026-02-01", "2026-02-02",
        "2026-02-03", "2026-02-04", "2026-02-05", "2026-03-01",
        "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05"
    ],
    "revenue": [
        1000, 1200, 1100, 1300,
        1250, 1400, 1350, 1500,
        1450, 1600, 1800, 1900,
        1750, 2000, 2100, 2500,
        2700, 2600, 2800, 3000
    ]
})

# Convert date column into datetime
df["date"] = pd.to_datetime(df["date"])

# Set date as index
df = df.set_index("date")

print("DataFrame:")
print(df)

# Confirm index datatype
print("\nIndex dtype:")
print(df.index.dtype)


# ============================================================
# 2. DAILY DATA -> MONTHLY TOTAL
# ============================================================

monthly = df.resample("ME").sum()

print("\nMonthly Revenue:")
print(monthly)


# ============================================================
# 3. 3-PERIOD ROLLING AVERAGE
# ============================================================

monthly["rolling_avg"] = monthly["revenue"].rolling(window=3).mean()

# First two values are NaN because a 3-period average
# needs 3 previous/current observations to calculate the mean.

print("\n3-Month Rolling Average:")
print(monthly)


# ============================================================
# 4. PREVIOUS PERIOD VALUE USING shift()
# ============================================================

monthly["previous_month_revenue"] = monthly["revenue"].shift(1)

print("\nPrevious Month Revenue:")
print(monthly)


# Manually verify February's previous value
feb_revenue = monthly.loc["2026-02-28", "revenue"]
feb_previous = monthly.loc["2026-02-28", "previous_month_revenue"]

jan_revenue = monthly.loc["2026-01-31", "revenue"]

print("\nManual Verification:")
print("January Revenue:", jan_revenue)
print("February Previous Month Revenue:", feb_previous)

assert feb_previous == jan_revenue

print("Verification successful!")


# ============================================================
# 5. MONTH-OVER-MONTH GROWTH USING pct_change()
# ============================================================

monthly["MoM_growth_%"] = monthly["revenue"].pct_change() * 100

print("\nMonth-over-Month Growth:")
print(monthly)


# Find month with highest growth
highest_growth_month = monthly["MoM_growth_%"].idxmax()
highest_growth_rate = monthly["MoM_growth_%"].max()

print("\nHighest Growth:")
print("Month:", highest_growth_month.strftime("%B %Y"))
print("Growth Rate:", round(highest_growth_rate, 2), "%")