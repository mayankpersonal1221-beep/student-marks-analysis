import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/students.csv")
print("Student Data:\n", df)
print("\nAverage Marks:")
print(df.mean(numeric_only=True))
df["Total"] = df[["Maths","Science","English"]].sum(axis=1)
df["Percentage"] = df["Total"] / 3
print("\nUpdated Data:\n", df)

plt.bar(df["Name"], df["Percentage"])
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.title("Student Performance Analysis")
plt.show()