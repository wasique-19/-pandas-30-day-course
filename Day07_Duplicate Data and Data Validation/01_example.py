import pandas as pd

# ============================================================
# 1. duplicated() - Identify exact duplicate rows
# ============================================================

print("1. IDENTIFY DUPLICATE ROWS")

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Bob", "Diana", "Bob"],
    "Age": [25, 30, 28, 30, 35, 30],
    "City": ["Delhi", "Mumbai", "Pune", "Mumbai", "Delhi", "Mumbai"]
})

print("Original DataFrame:")
print(df)

# duplicated() returns True for rows that are duplicates
duplicate_rows = df.duplicated()

print("\nDuplicate rows:")
print(duplicate_rows)

print("\nDuplicate records:")
print(df[df.duplicated()])


# ============================================================
# 2. drop_duplicates() - Remove duplicate rows
# ============================================================

print("\n2. REMOVE DUPLICATE ROWS")

clean_df = df.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(clean_df)

print("\nOriginal row count:", len(df))
print("\nRow count after removing duplicates:", len(clean_df))


# ============================================================
# 3. subset= - Detect duplicate Email values
# ============================================================

print("\n3. FIND DUPLICATES USING EMAIL")

customers = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Email": [
        "alice@gmail.com",
        "bob@gmail.com",
        "alice@gmail.com",
        "diana@gmail.com"
    ],
    "City": ["Delhi", "Mumbai", "Pune", "Chennai"]
})

print("Customer DataFrame:")
print(customers)

# Check duplicates based ONLY on Email
email_duplicates = customers.duplicated(subset=["Email"])

print("\nDuplicate Emails:")
print(email_duplicates)

print("\nRecords with duplicate Emails:")
print(customers[customers.duplicated(subset=["Email"], keep=False)])


# ============================================================
# 4. unique() - Find inconsistent categorical labels
# ============================================================

print("\n4. STANDARDIZE INCONSISTENT LABELS")

survey = pd.DataFrame({
    "Customer": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Subscribed": ["yes", "Yes", "YES", "no", "NO"]
})

print("\nOriginal values:")
print(survey)

# Check unique values
print("\nUnique values before standardization:")
print(survey["Subscribed"].unique())

# Standardize all values:
# "yes", "Yes", "YES" -> "Yes"
# "no", "No", "NO"   -> "No"
survey["Subscribed"] = (
    survey["Subscribed"]
    .str.strip()
    .str.lower()
    .map({"yes": "Yes", "no": "No"})
)

print("\nUnique values after standardization:")
print(survey["Subscribed"].unique())

print("\nStandardized DataFrame:")
print(survey)


# ============================================================
# 5. Remove duplicate Emails while keeping earliest SignupDate
# ============================================================

print("\n5. KEEP EARLIEST SIGNUP DATE FOR EACH EMAIL")

customer_data = pd.DataFrame({
    "Customer": [
        "Alice", "Bob", "Alice", "Charlie",
        "Bob", "Diana", "Charlie"
    ],
    "Email": [
        "alice@gmail.com",
        "bob@gmail.com",
        "alice@gmail.com",
        "charlie@gmail.com",
        "bob@gmail.com",
        "diana@gmail.com",
        "charlie@gmail.com"
    ],
    "SignupDate": [
        "2024-05-10",
        "2024-03-15",
        "2024-01-20",
        "2024-06-10",
        "2024-02-01",
        "2024-04-05",
        "2024-05-01"
    ]
})

# Convert SignupDate from string to datetime
customer_data["SignupDate"] = pd.to_datetime(
    customer_data["SignupDate"]
)

print("\nOriginal Customer DataFrame:")
print(customer_data)

# Step 1: Sort by Email and SignupDate
# Earliest date will come first for each email.
sorted_customers = customer_data.sort_values(
    by=["Email", "SignupDate"],
    ascending=[True, True]
)

# Step 2: Remove duplicate emails
# keep="first" keeps the earliest signup date because
# the data was sorted in ascending date order.
unique_customers = sorted_customers.drop_duplicates(
    subset=["Email"],
    keep="first"
)

# Step 3: Sort by Email for a clean final report
unique_customers = unique_customers.sort_values(
    by="Email"
).reset_index(drop=True)

print("\nFinal DataFrame:")
print(unique_customers)