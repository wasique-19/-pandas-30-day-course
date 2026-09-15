import pandas as pd
from io import StringIO

# Simulate a CSV with different missing-value markers
csv_data = StringIO("""Name,Age,City,Salary
Alice,25,Delhi,45000
Bob,NA,Mumbai,60000
Charlie,--,,55000
Diana,35,NA,--
Ethan,,Pune,70000
""")

# Treat "NA", "--", and empty strings as missing values
df = pd.read_csv(
    csv_data,
    na_values=["NA", "--", ""],
    keep_default_na=True
)

print(df)

# Confirm missing values
print("\nMissing values:")
print(df.isna())