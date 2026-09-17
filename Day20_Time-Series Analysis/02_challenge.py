import pandas as pd

# ============================================================
# 1. CREATE 30 DAYS OF DAILY SALES DATA
# ============================================================

# Create 30 consecutive dates
dates = pd.date_range(start="2026-01-01", periods=30, freq="D")

# Manually constructed daily sales values
sales = [
    100, 120, 115, 130, 125,
    140, 150, 135, 160, 155,
    170, 165, 180, 175, 190,
    200, 195, 210, 205, 220,
    230, 225, 240, 250, 245,
    260, 280, 275, 300, 350
]

# Create DataFrame
df = pd.DataFrame({
    "date": dates,
    "sales": sales
})

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Set date as DatetimeIndex
df = df.set_index("date")


# ============================================================
# 2. CHECK THE DATAFRAME AND DATETIMEINDEX
# ============================================================

print("=" * 60)
print("DAILY SALES DATA")
print("=" * 60)

print(df)

print("\nIndex dtype:")
print(df.index.dtype)


# ============================================================
# 3. WEEKLY SALES TOTALS
# ============================================================

weekly_sales = df.resample("W").sum()

print("\n" + "=" * 60)
print("WEEKLY SALES TOTALS")
print("=" * 60)

print(weekly_sales)


# ============================================================
# 4. 7-DAY ROLLING AVERAGE
# ============================================================

df["7_day_rolling_avg"] = df["sales"].rolling(window=7).mean()

# The first 6 values are NaN because a 7-day average
# requires 7 observations before the first average can be calculated.

print("\n" + "=" * 60)
print("7-DAY ROLLING AVERAGE")
print("=" * 60)

print(df[["sales", "7_day_rolling_avg"]])


# ============================================================
# 5. DAY-OVER-DAY PERCENTAGE CHANGE
# ============================================================

df["daily_pct_change"] = df["sales"].pct_change() * 100

print("\n" + "=" * 60)
print("DAY-OVER-DAY PERCENTAGE CHANGE")
print("=" * 60)

print(df[["sales", "daily_pct_change"]])


# ============================================================
# 6. FIND THE DAY WITH LARGEST PERCENTAGE INCREASE
# ============================================================

best_day = df["daily_pct_change"].idxmax()
best_growth = df["daily_pct_change"].max()
best_day_sales = df.loc[best_day, "sales"]

previous_day = df.index[df.index.get_loc(best_day) - 1]
previous_sales = df.loc[previous_day, "sales"]


# ============================================================
# 7. FINAL HIGHLIGHTED ANSWER
# ============================================================

print("\n" + "=" * 60)
print("🏆 BEST DAY")
print("=" * 60)

print(f"Date: {best_day.strftime('%Y-%m-%d')}")
print(f"Sales: {best_day_sales}")
print(f"Previous Day Sales: {previous_sales}")
print(f"Percentage Increase: {best_growth:.2f}%")

print("\n🏆 HIGHLIGHTED ANSWER:")
print(
    f"{best_day.strftime('%B %d, %Y')} had the largest "
    f"day-over-day sales increase: {best_growth:.2f}%."
)