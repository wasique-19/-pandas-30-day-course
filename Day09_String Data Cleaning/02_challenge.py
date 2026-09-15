import pandas as pd

# ============================================================
# CUSTOMER DATA CLEANING ASSIGNMENT
# ============================================================

print("=" * 75)
print("CUSTOMER DATA CLEANING")
print("=" * 75)


# ============================================================
# STEP 1: CREATE MESSY CUSTOMER DATA
# ============================================================

customers = pd.DataFrame({
    "FullName": [
        "  alice smith  ",
        "BOB JOHNSON",
        "  charlie brown",
        "DIANA   WILSON ",
        " ethan davis",
        "FARAH KHAN  ",
        "  george miller",
        "HINA SHARMA "
    ],

    "Email": [
        "  Alice@Gmail.com ",
        "BOB@YAHOO.COM",
        " charlie@gmail.com",
        "DIANA@OUTLOOK.COM ",
        "  ethan@GMAIL.COM",
        "farah@yahoo.com  ",
        " GEORGE@Gmail.COM ",
        "hina@OUTLOOK.com"
    ],

    "Phone": [
        "(212) 555-1234",
        "415-555-5678",
        "650 555 9012",
        "(305)555-3456",
        "718- 555 -7890",
        " 404 555 1122 ",
        "(202) 555 3344",
        "312-555-7788"
    ]
})


# ============================================================
# STEP 2: PRINT ORIGINAL DATA
# ============================================================

print("\n" + "=" * 75)
print("BEFORE CLEANING")
print("=" * 75)

print(customers)


# ============================================================
# STEP 3: SPLIT FULLNAME
#
# strip() -> extra spaces at beginning/end remove
# split() -> multiple spaces ko automatically handle karta hai
# expand=True -> separate columns create karta hai
# ============================================================

name_parts = customers["FullName"].str.strip().str.split(
    r"\s+",
    expand=True
)

customers["FirstName"] = name_parts[0]
customers["LastName"] = name_parts[1]


# ============================================================
# STEP 4: CLEAN EMAIL
#
# strip() -> extra whitespace remove
# lower() -> lowercase mein convert
# ============================================================

customers["CleanEmail"] = (
    customers["Email"]
    .str.strip()
    .str.lower()
)


# ============================================================
# STEP 5: CREATE GMAIL BOOLEAN FLAG
#
# Gmail address -> True
# Other email -> False
#
# starts/contains Gmail ko case-insensitive banane ke liye
# email ko pehle lowercase kiya gaya hai.
# ============================================================

customers["IsGmail"] = customers["CleanEmail"].str.contains(
    "@gmail.",
    regex=False,
    na=False
)


# ============================================================
# STEP 6: NORMALIZE PHONE NUMBERS
#
# Regex:
# \D+ -> one or more NON-DIGIT characters
#
# Isse:
# spaces, -, (, ) etc. remove ho jayenge.
#
# Example:
# "(212) 555-1234"
#        ↓
# "2125551234"
# ============================================================

customers["CleanPhone"] = (
    customers["Phone"]
    .str.replace(r"\D+", "", regex=True)
)


# ============================================================
# STEP 7: BEFORE / AFTER COMPARISON
# ============================================================

print("\n" + "=" * 75)
print("BEFORE / AFTER COMPARISON")
print("=" * 75)

print(
    customers[
        [
            "FullName",
            "FirstName",
            "LastName",
            "Email",
            "CleanEmail",
            "IsGmail",
            "Phone",
            "CleanPhone"
        ]
    ]
)


# ============================================================
# STEP 8: FINAL CLEANED DATAFRAME
# ============================================================

print("\n" + "=" * 75)
print("FINAL CLEANED DATAFRAME")
print("=" * 75)

print(
    customers[
        [
            "FirstName",
            "LastName",
            "CleanEmail",
            "IsGmail",
            "CleanPhone"
        ]
    ]
)


# ============================================================
# STEP 9: CHECK FINAL DTYPES
# ============================================================

print("\n" + "=" * 75)
print("FINAL DATA TYPES")
print("=" * 75)

print(
    customers[
        [
            "FirstName",
            "LastName",
            "CleanEmail",
            "IsGmail",
            "CleanPhone"
        ]
    ].dtypes
)