import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Input Data Creation
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# (a) Clean Name column using .str.strip() and .str.title()
df["Name"] = df["Name"].str.strip().str.title()

# (b) Convert Marks to numeric and fill absent student's mark with the mean of the others
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
mean_mark = df["Marks"].mean().round(1)
df["Marks"] = df["Marks"].fillna(mean_mark)

# (c) Print cleaned DataFrame
print("Cleaned DataFrame:")
print(df)

# (d) Draw bar plot of marks per student
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="black")
plt.title("Student Marks Distribution")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save image and display
plt.savefig("marks_bar.png")
plt.show()
print("Saved marks_bar.png")
