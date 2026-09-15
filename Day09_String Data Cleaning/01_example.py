import pandas as pd

# ============================================================
# 1. EASY
# CLEAN NAME COLUMN
# strip() -> extra spaces remove
# title() -> proper capitalization
# ============================================================

print("=" * 70)
print("1. CLEAN NAME COLUMN")
print("=" * 70)

df = pd.DataFrame({
    "Name": [
        "  alice smith",
        "BOB JOHNSON  ",
        "  charlie brown  ",
        "DIANA WILSON",
        "  ethan davis"
    ]
})

print("Before cleaning:")
print(df)

df["Name"] = (
    df["Name"]
    .str.strip()
    .str.title()
)

print("\nAfter cleaning:")
print(df)


# ============================================================
# 2. EASY
# FIND EMAILS CONTAINING "YAHOO"
# case=False -> uppercase/lowercase ignore
# na=False -> missing values safely treated as False
# ============================================================

print("\n" + "=" * 70)
print("2. FIND YAHOO EMAIL ADDRESSES")
print("=" * 70)

emails = pd.DataFrame({
    "Email": [
        "alice@gmail.com",
        "bob@yahoo.com",
        "charlie@YAHOO.com",
        "diana@outlook.com",
        "ethan@yahoo.co.in",
        "farah@GMAIL.COM"
    ]
})

print("All emails:")
print(emails)

yahoo_emails = emails[
    emails["Email"].str.contains(
        "yahoo",
        case=False,
        na=False
    )
]

print("\nYahoo emails:")
print(yahoo_emails)


# ============================================================
# 3. MEDIUM
# SPLIT FULL NAME INTO FIRST NAME AND LAST NAME
# expand=True -> creates separate columns
# ============================================================

print("\n" + "=" * 70)
print("3. SPLIT FULL NAME")
print("=" * 70)

people = pd.DataFrame({
    "FullName": [
        "Alice Smith",
        "Bob Johnson",
        "Charlie Brown",
        "Diana Wilson",
        "Ethan Davis"
    ]
})

print("Before splitting:")
print(people)

people[["FirstName", "LastName"]] = (
    people["FullName"]
    .str.split(expand=True)
)

print("\nAfter splitting:")
print(people)


# ============================================================
# 4. MEDIUM
# REMOVE ALL DIGITS FROM TEXT
#
# Regex pattern:
# \d  -> any digit from 0 to 9
# +   -> one or more digits
#
# regex=True -> pattern ko regular expression maana jayega
# ============================================================

print("\n" + "=" * 70)
print("4. REMOVE ALL DIGITS")
print("=" * 70)

data = pd.DataFrame({
    "Text": [
        "Product123",
        "Room45",
        "Item2026",
        "ABC123XYZ",
        "Order999"
    ]
})

print("Before removing digits:")
print(data)

data["Text"] = data["Text"].str.replace(
    r"\d+",
    "",
    regex=True
)

print("\nAfter removing digits:")
print(data)


# ============================================================
# 5. CHALLENGING
# EXTRACT AREA CODE FROM PHONE NUMBERS
#
# Format:
# (XXX) XXX-XXXX
#
# Regex:
# \(      -> opening parenthesis
# (\d{3}) -> capture exactly 3 digits
# \)      -> closing parenthesis
#
# str.extract() returns the captured group.
# ============================================================

print("\n" + "=" * 70)
print("5. EXTRACT PHONE AREA CODE")
print("=" * 70)

phones = pd.DataFrame({
    "Phone": [
        "(212) 555-1234",
        "(415) 555-5678",
        "(650) 555-9012",
        "(305) 555-3456",
        "(718) 555-7890"
    ]
})

print("Original phone numbers:")
print(phones)

phones["AreaCode"] = phones["Phone"].str.extract(
    r"\((\d{3})\)"
)

print("\nAfter extracting area code:")
print(phones)