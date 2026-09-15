import pandas as pd
from io import StringIO

# Simulate the raw CSV-like customer feedback export
raw_data = StringIO("""Export generated: Customer Feedback Report
Customer|Rating|Feedback
Alice|5|Excellent service
Bob|n/a|Good experience
Charlie|4|Very helpful staff
Diana|n/a|Average experience
Ethan|3|Could be better
Fiona|5|Outstanding service
""")

# Load and clean the data
df = pd.read_csv(
    raw_data,
    sep="|",
    skiprows=1,
    na_values="n/a"
)

# Print the clean DataFrame
print(df)