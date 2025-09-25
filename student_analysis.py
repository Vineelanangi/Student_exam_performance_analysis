# 📌 Student Exam Performance Analysis
# Author: Nangi Vineela
# Description: Analyze students' exam performance using Pandas, Numpy, Matplotlib, Seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load Dataset
df = pd.read_csv("StudentsPerformance.csv")
print("✅ Dataset Loaded Successfully!\n")
print(df.head())

# 2️⃣ Basic Info
print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Statistical Summary:")
print(df.describe())

# 3️⃣ Check Missing Values
print("\n📌 Missing Values:")
print(df.isnull().sum())

# 4️⃣ Data Analysis

# Average scores by gender
avg_scores = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
print("\n📊 Average Scores by Gender:\n", avg_scores)

# Plot 1: Gender vs Average Score
plt.figure(figsize=(8, 5))
avg_scores.plot(kind='bar', figsize=(8, 5))
plt.title("Average Scores by Gender")
plt.ylabel("Average Score")
plt.xlabel("Gender")
plt.legend(loc='lower right')
plt.savefig("gender_avg_scores.png")
plt.show()
plt.close()   # ✅ Close figure to prevent overlapping

# Plot 2: Math Score Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["math score"], kde=True, bins=20)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.savefig("math_score_distribution.png")
plt.show()
plt.close()

# Plot 3: Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()
plt.close()

print("\n✅ Analysis Completed. All 3 charts saved as PNG files.")