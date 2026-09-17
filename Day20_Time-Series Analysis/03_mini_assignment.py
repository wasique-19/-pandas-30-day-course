import pandas as pd

# ============================================================
# 1. CREATE 21 DAYS OF DAILY REVENUE DATA
# ============================================================

dates = pd.date_range("2026-01-01", periods=21, freq="D")

revenue = [
    1000, 1100, 1050, 1200, 1250, 1300, 1350,
    1400, 1450, 1500, 1000, 1550, 1600, 1650,
    1700, 1750, 1800, 1200, 1900, 1950, 2000
]

df = pd.DataFrame({
    "revenue": revenue
}, index=dates)

# Confirm that the index is a proper DatetimeIndex
print("Index type:", type(df.index))
print("Index dtype:", df.index.dtype)


# ============================================================
# 2. 7-DAY ROLLING AVERAGE
# ============================================================

df["7_day_rolling_avg"] = df["revenue"].rolling(window=7).mean()

print("\n" + "=" * 60)
print("7-DAY ROLLING AVERAGE")
print("=" * 60)

print(df[["revenue", "7_day_rolling_avg"]])


# ============================================================
# 3. WEEKLY REVENUE TOTALS
# ============================================================

weekly_totals = df["revenue"].resample("W").sum()

print("\n" + "=" * 60)
print("WEEKLY REVENUE TOTALS")
print("=" * 60)

print(weekly_totals)


# ============================================================
# 4. DAY-OVER-DAY PERCENTAGE CHANGE
# ============================================================

df["day_over_day_%"] = df["revenue"].pct_change() * 100

print("\n" + "=" * 60)
print("DAY-OVER-DAY PERCENTAGE CHANGE")
print("=" * 60)

print(df[["revenue", "day_over_day_%"]])


# ============================================================
# 5. SHARPEST SINGLE-DAY REVENUE DROP
# ============================================================

sharpest_drop_day = df["day_over_day_%"].idxmin()
sharpest_drop = df["day_over_day_%"].min()

# The sharpest drop occurred on 2026-01-11,
# when revenue fell from 1500 to 1000, a drop of 33.33%.