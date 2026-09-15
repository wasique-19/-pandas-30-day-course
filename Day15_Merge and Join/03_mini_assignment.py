import pandas as pd

# ============================================================
# 1. Students DataFrame
# Student 104 has NO enrollment
# ============================================================

students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "Diana"]
})


# ============================================================
# 2. Enrollments DataFrame
# ============================================================

enrollments = pd.DataFrame({
    "StudentID": [101, 101, 102, 103],
    "CourseID": ["C01", "C02", "C03", "C01"]
})


# ============================================================
# 3. Courses DataFrame
# C04 has NO enrolled students
# ============================================================

courses = pd.DataFrame({
    "CourseID": ["C01", "C02", "C03", "C04"],
    "CourseName": [
        "Python",
        "Pandas",
        "SQL",
        "Machine Learning"
    ]
})


# ============================================================
# 4. Merge Students + Enrollments
# LEFT JOIN preserves students with no courses
# ============================================================

student_enrollment = pd.merge(
    students,
    enrollments,
    on="StudentID",
    how="left"
)


# ============================================================
# 5. Merge with Courses
# OUTER JOIN preserves:
# - students with no enrollment
# - courses with no students
# ============================================================

final_df = pd.merge(
    student_enrollment,
    courses,
    on="CourseID",
    how="outer"
)


# ============================================================
# 6. Arrange columns
# ============================================================

final_df = final_df[
    ["StudentID", "Name", "CourseID", "CourseName"]
]


# ============================================================
# 7. Print final result
# ============================================================

print("=" * 60)
print("FINAL STUDENT-COURSE TABLE")
print("=" * 60)
print(final_df)