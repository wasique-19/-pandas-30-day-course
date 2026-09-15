import pandas as pd

# ============================================================
# CREATE DATAFRAME
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
        " charlie@GMAIL.COM",
        "DIANA@Outlook.COM ",
        "  Ethan@Gmail.Com",
        "FARAH@YAHOO.COM  ",
        " George@GMAIL.COM ",
        "HINA@Outlook.COM"
    ]
})

# ============================================================
# CLEAN FULL NAME
# strip() -> remove extra spaces from beginning/end
# split() -> split first and last name
# title() -> proper capitalization
# ============================================================

name_parts = (
    customers["FullName"]
    .str.strip()
    .str.split(r"\s+", expand=True)
)

customers["FirstName"] = name_parts[0].str.title()
customers["LastName"] = name_parts[1].str.title()


# ============================================================
# CLEAN EMAIL
# strip() -> remove extra spaces
# lower() -> convert to lowercase
# ============================================================

customers["CleanEmail"] = (
    customers["Email"]
    .str.strip()
    .str.lower()
)


# ============================================================
# CREATE GMAIL BOOLEAN FLAG
# True  -> gmail.com
# False -> other email provider
# ============================================================

customers["IsGmail"] = customers["CleanEmail"].str.endswith(
    "@gmail.com",
    na=False
)


# ============================================================
# PRINT FULLY CLEANED DATAFRAME
# ============================================================

print("=" * 70)
print("FULLY CLEANED CUSTOMER DATA")
print("=" * 70)

print(
    customers[
        [
            "FirstName",
            "LastName",
            "CleanEmail",
            "IsGmail"
        ]
    ]
)