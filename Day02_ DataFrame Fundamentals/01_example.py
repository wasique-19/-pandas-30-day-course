import pandas as pd
import numpy as np

# Dictionary -> DataFrame
df = pd.DataFrame({
    "Employee": ["Asha", "Rahul", "Vikram", "Neha"],
    "Department": ["Sales", "IT", "Sales", "HR"],
    "Salary": [50000, 70000, 55000, 60000]
})

print("DATAFRAME")
print(df)

print("\nOne column:")
print(df["Salary"])

print("\nMultiple columns:")
print(df[["Employee", "Salary"]])

print("\nFirst two rows:")
print(df.head(2))

print("\nLast two rows:")
print(df.tail(2))

print("\nRandom row:")
print(df.sample(1))

print("\nShape:", df.shape)