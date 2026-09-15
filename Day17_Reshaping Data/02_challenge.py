import pandas as pd

# ============================================================
# 1. CREATE WIDE-FORMAT STUDENT DATA
# ============================================================

students = pd.DataFrame({
    "StudentName": [
        "Alice", "Bob", "Charlie",
        "Diana", "Ethan", "Fiona"
    ],
    "Math": [85, 72, 90, 65, 78, 95],
    "Science": [88, 75, 82, 70, 80, 92],
    "English": [90, 68, 85, 75, 82, 88]
})

print("=" * 70)
print("ORIGINAL WIDE DATA")
print("=" * 70)
print(students)


# ============================================================
# 2. MELT WIDE → LONG
# ============================================================

long_data = students.melt(
    id_vars="StudentName",
    var_name="Subject",
    value_name="Score"
)

print("\n" + "=" * 70)
print("1. LONG-FORMAT DATA")
print("=" * 70)
print(long_data)


# ============================================================
# 3. COMPUTE AVERAGE SCORE PER SUBJECT
# ============================================================

subject_average = (
    long_data
    .groupby("Subject")["Score"]
    .mean()
    .round(2)
)

print("\n" + "=" * 70)
print("2. AVERAGE SCORE PER SUBJECT")
print("=" * 70)
print(subject_average)


# ============================================================
# 4. USE transform() TO PUT SUBJECT AVERAGE
#    ON EVERY STUDENT'S ROW
# ============================================================

long_data["SubjectAverage"] = (
    long_data
    .groupby("Subject")["Score"]
    .transform("mean")
    .round(2)
)


# ============================================================
# 5. COMPARE EACH SCORE WITH SUBJECT AVERAGE
# ============================================================

long_data["Performance"] = (
    long_data["Score"] >= long_data["SubjectAverage"]
).map({
    True: "Above/Average",
    False: "Below Average"
})


print("\n" + "=" * 70)
print("3. LONG DATA WITH SUBJECT AVERAGE & PERFORMANCE")
print("=" * 70)
print(long_data)


# ============================================================
# 6. PIVOT BACK TO WIDE FORMAT
#    Score for each subject
# ============================================================

score_wide = long_data.pivot(
    index="StudentName",
    columns="Subject",
    values="Score"
).reset_index()

score_wide.columns.name = None


# ============================================================
# 7. PIVOT PERFORMANCE INTO WIDE FORMAT
# ============================================================

performance_wide = long_data.pivot(
    index="StudentName",
    columns="Subject",
    values="Performance"
).reset_index()

performance_wide.columns = [
    "StudentName",
    "Math_Performance",
    "Science_Performance",
    "English_Performance"
]


# ============================================================
# 8. COMBINE SCORE + PERFORMANCE TABLES
# ============================================================

final_wide = pd.merge(
    score_wide,
    performance_wide,
    on="StudentName"
)


# ============================================================
# 9. PRINT FINAL WIDE TABLE
# ============================================================

print("\n" + "=" * 70)
print("4. FINAL WIDE COMPARISON TABLE")
print("=" * 70)
print(final_wide)