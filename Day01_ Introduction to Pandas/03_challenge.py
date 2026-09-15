import pandas as pd

#  Create a customer DataFrame containing 10 customers, their age, city, and spending,
#  Determine the customer with the highest spending and calculate average spending.


customers = pd.DataFrame({
    "Customer": ["Alice", "Bob", "Charlie", "Diana", "Ethan",
                 "Fiona", "George", "Hannah", "Ivan", "Julia"],
    "Age": [25, 32, 28, 41, 35, 29, 45, 31, 38, 27],
    "City": ["Delhi", "Mumbai", "Chennai", "Delhi", "Pune",
             "Mumbai", "Bangalore", "Delhi", "Pune", "Chennai"],
    "Spending": [1200, 2500, 1800, 3200, 2100,
                 1500, 4000, 2750, 2300, 1600]
})

print("\nDataFrame")
print(customers)

highest_spender = customers["Spending"].max()
print("\nHighest spending:", highest_spender)

average_spending = customers["Spending"].mean()
print("\nAverage spending:", average_spending)