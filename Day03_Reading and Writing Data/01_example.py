#  Example 1 — Writing then Reading a CSV

import pandas as pd

# Step 1: Create a DataFrame
df = pd.DataFrame({
    "OrderID": [1001, 1002, 1003],
    "Product": ["Notebook", "Pen", "Eraser"],
    "Amount": [50, 10, 5]
})

# Step 2: Write it to CSV (index=False avoids an extra unnamed column)
df.to_csv("orders.csv", index=False)

# Step 3: Read it back in
df_loaded = pd.read_csv("orders.csv")
print(df_loaded)