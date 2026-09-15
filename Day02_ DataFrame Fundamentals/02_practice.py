import pandas as pd

#  Create a five-row employee DataFrame. 

employees = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "Salary": [45000, 60000, 55000, 65000, 58000]
})

print("DATAFRAME")
print(employees) 

#  Select the Name column

print("\nOne column:")
print(employees["Name"])

#  Select three columns

print("\nThree column:")
print(employees[["Name", "Department", "Salary"]])

#  Display three random rows

print("\nrandom three row:")
print(employees.sample(3))
