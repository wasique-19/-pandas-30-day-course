import pandas as pd
import numpy as np

# ============================================================
# 1. CREATE DATAFRAME
# ============================================================

students = pd.DataFrame({
    "Student": [
        "Ali", "Sara", "John", "Emma",
        "David", "Ayesha", "Michael", "Sana"
    ],
    "Marks": [
        85, 110, 72, 35,
        95, 48, 67, 102
    ]
})

# ============================================================
# 2. CREATE RANK COLUMN
# Highest marks = Rank 1
# ============================================================

students["Rank"] = students["Marks"].rank(
    ascending=False,
    method="min"
).astype(int)

# ============================================================
# 3. CREATE PASSFAIL COLUMN USING np.where()
#
# Marks >= 40 -> Pass
# Marks < 40  -> Fail
# ============================================================

students["PassFail"] = np.where(
    students["Marks"] >= 40,
    "Pass",
    "Fail"
)

# ============================================================
# 4. CREATE CAPPED MARKS USING where()
#
# Marks <= 100 -> Keep original marks
# Marks > 100  -> Replace with 100
# ============================================================

students["Marks_Capped"] = students["Marks"].where(
    students["Marks"] <= 100,
    100
)

# ============================================================
# 5. SORT BY RANK
# ============================================================

students = students.sort_values(
    by="Rank"
).reset_index(drop=True)

# ============================================================
# 6. PRINT FINAL DATAFRAME
# ============================================================

print("=" * 75)
print("FINAL STUDENT DATA")
print("=" * 75)

print(students)