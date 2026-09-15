import pandas as pd

# ============================================================
# JOB APPLICANTS DATA
# ============================================================

applicants = pd.DataFrame({
    "Applicant": [
        "Ali", "Sara", "John", "Emma", "David",
        "Ayesha", "Michael", "Sana", "Robert", "Fatima"
    ],
    "YearsExperience": [
        1, 3, 6, 8, 2,
        5, 4, 7, 1, 10
    ],
    "EducationLevel": [
        "Bachelor's", "Bachelor's", "Master's", "PhD", "Master's",
        "Bachelor's", "Master's", "PhD", "Bachelor's", "PhD"
    ],
    "TechnicalScore": [
        45, 65, 85, 92, 72,
        88, 78, 95, 90, 82
    ]
})


# ============================================================
# ELIGIBILITY FUNCTION
# ============================================================

def check_eligibility(row):

    experience = row["YearsExperience"]
    education = row["EducationLevel"]
    score = row["TechnicalScore"]

    # --------------------------------------------------------
    # NOT ELIGIBLE
    # --------------------------------------------------------
    # Minimum requirement:
    # Experience must be at least 2 years
    # Technical score must be at least 50
    # --------------------------------------------------------

    if experience < 2 or score < 50:
        return "Not Eligible"

    # --------------------------------------------------------
    # HIGHLY ELIGIBLE
    # --------------------------------------------------------
    # Strong candidate:
    # 5+ years experience
    # Master's or PhD
    # Technical score 80+
    # --------------------------------------------------------

    elif (
        experience >= 5
        and education in ["Master's", "PhD"]
        and score >= 80
    ):
        return "Highly Eligible"

    # --------------------------------------------------------
    # ELIGIBLE
    # --------------------------------------------------------

    else:
        return "Eligible"


# ============================================================
# APPLY FUNCTION ROW-WISE
# ============================================================

applicants["Eligibility"] = applicants.apply(
    check_eligibility,
    axis=1
)


# ============================================================
# PRINT FINAL DATAFRAME
# ============================================================

print("=" * 90)
print("JOB APPLICANT ELIGIBILITY")
print("=" * 90)

print(applicants)