#  Example 3 — Excel and JSON Round Trip

import pandas as pd

df = pd.DataFrame({
    "Employee": ["Asha", "Ravi"],
    "Department": ["Finance", "IT"],
    "Salary": [65000, 71000]
})

# Write to Excel
df.to_excel("employees.xlsx", index=False, sheet_name="Staff")

# Read it back
df_excel = pd.read_excel("employees.xlsx", sheet_name="Staff")
print(df_excel)

# Write to JSON
df.to_json("employees.json", orient="records")

# Read it back
df_json = pd.read_json("employees.json")
print(df_json)