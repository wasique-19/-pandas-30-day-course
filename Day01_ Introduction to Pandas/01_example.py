import pandas as pd

# Create a Series
sales = pd.Series([1000, 1500, 1200], index=["A", "B", "C"])

print("Series:")
print(sales)

# Create a DataFrame
df = pd.DataFrame({
    "Name": ["Asha", "Rahul", "Priya"],
    "Age": [25, 30, 28],
    "Sales": [1000, 1500, 1200]
})

print("\nDataFrame:")
print(df)

print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

print("\nInfo:")
df.info()

print("\nStatistics:")
print(df.describe())