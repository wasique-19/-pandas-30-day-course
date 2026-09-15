import pandas as pd

# ============================================================
# 1. EASY
# Write a function that doubles a number
# Apply it to a numeric column using apply()
# ============================================================

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Salary": [50000, 60000, 55000, 70000]
})

# Function to double a number
def double_number(x):
    return x * 2

# Apply function to Salary column
df["DoubleSalary"] = df["Salary"].apply(double_number)

print("1. Double Salary")
print(df)


# ============================================================
# 2. EASY
# Use map() with a dictionary
# Convert M/F into Male/Female
# ============================================================

students = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Emma"],
    "Gender": ["M", "F", "M", "F"]
})

# Dictionary for conversion
gender_map = {
    "M": "Male",
    "F": "Female"
}

# map() replaces values according to dictionary
students["Gender"] = students["Gender"].map(gender_map)

print("\n2. Gender Conversion")
print(students)


# ============================================================
# 3. MEDIUM
# Categorize Age:
# Under 18  -> Minor
# 18 or more -> Adult
# Use apply()
# ============================================================

people = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Emma", "David"],
    "Age": [15, 22, 17, 30, 18]
})

# Function to categorize age
def age_category(age):
    if age < 18:
        return "Minor"
    else:
        return "Adult"

# Apply function to Age column
people["Category"] = people["Age"].apply(age_category)

print("\n3. Age Category")
print(people)


# ============================================================
# 4. MEDIUM
# Use apply(axis=1) to combine FirstName + LastName
# ============================================================

names = pd.DataFrame({
    "FirstName": ["Ali", "Sara", "John", "Emma"],
    "LastName": ["Khan", "Ali", "Smith", "Jones"]
})

# axis=1 means process one row at a time
def combine_name(row):
    return row["FirstName"] + " " + row["LastName"]

# Create FullName column
names["FullName"] = names.apply(combine_name, axis=1)

print("\n4. Full Name")
print(names)


# ============================================================
# 5. CHALLENGING
# Calculate shipping fee using Weight and Distance
#
# Weight rates:
#   <= 5 kg   -> ₹50
#   <= 10 kg  -> ₹80
#   > 10 kg   -> ₹120
#
# Distance rates:
#   <= 100 km -> ₹20
#   <= 500 km -> ₹50
#   > 500 km  -> ₹100
#
# Total Shipping Fee = Weight Fee + Distance Fee
#
# Use apply(axis=1)
# ============================================================

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "Weight": [3, 7, 12, 5, 15],
    "Distance": [50, 200, 600, 100, 800]
})

# Function calculates shipping fee for each row
def calculate_shipping(row):

    # -------------------------
    # Calculate weight fee
    # -------------------------
    if row["Weight"] <= 5:
        weight_fee = 50

    elif row["Weight"] <= 10:
        weight_fee = 80

    else:
        weight_fee = 120

    # -------------------------
    # Calculate distance fee
    # -------------------------
    if row["Distance"] <= 100:
        distance_fee = 20

    elif row["Distance"] <= 500:
        distance_fee = 50

    else:
        distance_fee = 100

    # Total fee
    return weight_fee + distance_fee


# Apply function row-wise
orders["ShippingFee"] = orders.apply(
    calculate_shipping,
    axis=1
)

print("\n5. Shipping Fee")
print(orders)