#  Example 2 — Reading CSV with Custom Parameters

import pandas as pd
from io import StringIO

# Simulating a messy CSV using semicolons and custom missing-value markers
raw_data = """OrderID;Product;Amount
1001;Notebook;50
1002;Pen;N/A
1003;Eraser;5
"""

df = pd.read_csv(StringIO(raw_data), sep=";", na_values=["N/A"])
print(df)