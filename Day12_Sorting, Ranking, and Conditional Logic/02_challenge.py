import pandas as pd
import numpy as np

# ============================================================
# 1. CREATE DATAFRAME
# ============================================================

employees = pd.DataFrame({
    "Employee": [
        "Alice", "Bob", "Charlie", "Diana", "Ethan",
        "Fiona", "George", "Hannah", "Ian", "Julia"
    ],
    "PerformanceScore": [
        92, 78, 88, 65, 95,
        72, 85, 60, 90, 68
    ],
    "YearsAtCompany": [
        5, 2, 4, 6, 3,
        1, 7, 2, 4, 5
    ]
})

# ============================================================
# 2. CREATE BONUS ELIGIBILITY USING NESTED np.where()
# ============================================================

employees["Bonus Eligibility"] = np.where(
    # First condition:
    # Performance >= 85 AND Years >= 3
    (employees["PerformanceScore"] >= 85) &
    (employees["YearsAtCompany"] >= 3),

    "High Bonus",

    # If first condition is False,
    # check the second condition
    np.where(
        employees["PerformanceScore"] >= 70,
        "Standard Bonus",
        "No Bonus"
    )
)

# ============================================================
# 3. RANK EMPLOYEES BY PERFORMANCE SCORE
# ============================================================

employees["Rank"] = employees["PerformanceScore"].rank(
    ascending=False,
    method="min"
).astype(int)

# ============================================================
# 4. SORT BY PERFORMANCE SCORE
# ============================================================

employees = employees.sort_values(
    by="PerformanceScore",
    ascending=False
)

# ============================================================
# 5. SHOW TOP 3 EMPLOYEES
# ============================================================

top_3 = employees.head(3)

print("=" * 85)
print("TOP 3 EMPLOYEES BY PERFORMANCE SCORE")
print("=" * 85)

print(
    top_3[
        [
            "Rank",
            "Employee",
            "PerformanceScore",
            "YearsAtCompany",
            "Bonus Eligibility"
        ]
    ]
)