# 1. Business problem statement + 3 objectives

""" **Business Problem Statement:**
A fitness application collects information about its users, their workout activities, and their daily health metrics, but the data is stored across multiple related tables. The business wants to understand user engagement, workout behavior, and health outcomes so that it can identify highly engaged users, improve personalized recommendations, and reduce user inactivity. A structured analytics project will combine these datasets, validate their quality, and generate actionable insights about fitness-app usage.

**Objectives:**

1. Measure user engagement by analyzing workout frequency, duration, and activity patterns.
2. Identify relationships between workout behavior and health metrics such as calories burned, steps, and heart rate.
3. Identify inactive or low-engagement users so the app can develop targeted retention and personalized fitness strategies."""


# 2. Create and inspect 3 related tables

import pandas as pd

# ============================================================
# TABLE 1: USERS
# ============================================================

users = pd.DataFrame({
    "UserID": [101, 102, 103, 104, 105, 106],
    "Name": [
        "Aarav", "Priya", "Rahul",
        "Sneha", "Vikram", "Ananya"
    ],
    "Age": [25, 31, 28, 35, 24, 29],
    "Gender": [
        "Male", "Female", "Male",
        "Female", "Male", "Female"
    ]
})


# ============================================================
# TABLE 2: WORKOUTS
# ============================================================

workouts = pd.DataFrame({
    "WorkoutID": [1, 2, 3, 4, 5, 6, 7, 8],
    "UserID": [
        101, 101, 102, 103,
        104, 105, 106, 102
    ],
    "WorkoutType": [
        "Running", "Cycling", "Yoga", "Running",
        "Strength", "Cycling", "Yoga", "Running"
    ],
    "DurationMinutes": [
        30, 45, 40, 35,
        50, 60, 30, 40
    ],
    "CaloriesBurned": [
        300, 450, 250, 350,
        500, 600, 200, 400
    ]
})


# ============================================================
# TABLE 3: HEALTH METRICS
# ============================================================

health_metrics = pd.DataFrame({
    "MetricID": [1001, 1002, 1003, 1004, 1005, 1006],
    "UserID": [101, 102, 103, 104, 105, 106],
    "Steps": [
        8500, 10000, 7200,
        9500, 6000, 8800
    ],
    "AvgHeartRate": [
        78, 82, 75, 80, 85, 77
    ],
    "SleepHours": [
        7.2, 6.8, 7.5, 7.0, 6.2, 7.8
    ]
})


# ============================================================
# PRINT SHAPE AND DTYPES
# ============================================================

tables = {
    "Users": users,
    "Workouts": workouts,
    "Health Metrics": health_metrics
}

print("=" * 70)
print("TABLE STRUCTURE")
print("=" * 70)

for name, table in tables.items():

    print(f"\n{name}")
    print("-" * 40)

    print("Shape:", table.shape)

    print("\nDtypes:")
    print(table.dtypes)


# 3. Data-quality loop

print("\n" + "=" * 70)
print("DATA QUALITY CHECK")
print("=" * 70)

for name, table in tables.items():

    print(f"\n{name}")
    print("-" * 40)

    # Missing values
    print("Missing values:")
    print(table.isnull().sum())

    # Total missing values
    print(
        "Total missing values:",
        table.isnull().sum().sum()
    )

    # Duplicate rows
    print(
        "Duplicate rows:",
        table.duplicated().sum()
    )


# 4. Primary-key and foreign-key relationships

"""
| Table            | Primary Key | Foreign Key | Relationship                    |
| ---------------- | ----------- | ----------- | ------------------------------- |
| `users`          | `UserID`    | —           | One user can have many workouts |
| `workouts`       | `WorkoutID` | `UserID`    | Links each workout to a user    |
| `health_metrics` | `MetricID`  | `UserID`    | Links health metrics to a user  |
"""

# The central relationship is:

"""
                 ┌──────────────┐
                 │    users     │
                 │──────────────│
                 │ PK: UserID   │
                 └──────┬───────┘
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
      ┌──────────────┐    ┌────────────────┐
      │   workouts   │    │ health_metrics │
      │──────────────│    │────────────────│
      │ PK: WorkoutID│    │ PK: MetricID   │
      │ FK: UserID   │    │ FK: UserID     │
      └──────────────┘    └────────────────┘
"""


# 5. Business questions the dataset can answer

"""
| # | Business question                                                                         | Required table(s)                       |
| - | ----------------------------------------------------------------------------------------- | --------------------------------------- |
| 1 | Which workout types burn the most calories on average?                                    | `workouts`                              |
| 2 | Which users are the most physically active based on workout frequency and duration?       | `users` + `workouts`                    |
| 3 | Is workout duration associated with calories burned?                                      | `workouts`                              |
| 4 | Do users with higher workout activity also have higher daily step counts?                 | `workouts` + `health_metrics`           |
| 5 | Which users have potentially low engagement based on workout activity and health metrics? | `users` + `workouts` + `health_metrics` |
"""