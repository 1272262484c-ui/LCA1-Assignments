
# Assignment 7: Data Visualization using Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV dataset
df = pd.read_csv("sample_data_assignment_07.csv")

# Display the dataset
print("Dataset:")
print(df)

# Line Plot: Python Marks
plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Plot: Maths Marks
plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.tight_layout()
plt.show()

# Scatter Plot: Maths vs Python
plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70)
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate correlation matrix
correlation = df[["Maths", "Python", "Attendance"]].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Heatmap
plt.figure(figsize=(6.5, 5))
sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    vmin=-1,
    vmax=1
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
