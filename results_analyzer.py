import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("results.csv")

print(df)
print(df.head())
print(df.describe())

df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)
#calculate across columns

print(df)
print(df.head())

#Data Analysis/patterns
df["Best Subject"] = df[["Math", "English", "Science"]].idxmax(axis=1)
print(df[["Name", "Best Subject"]])

df["Worst Subject"] = df[["Math", "English", "Science"]].idxmin(axis=1)
print(df[["Name", "Worst Subject"]])

#Perfromance categories
def performance (avg):
    if avg >=80:
        return "High"
    elif avg >=70:
        return "Medium"
    else:
        return "Low"

df["Performance"] = df["Average"].apply(performance)
print(df[["Name","Average", "Performance"]])

#Top students
top_students = df.sort_values(by="Average", ascending=False)
print("\n---Top Students---")
print(top_students[["Name", "Average", "Performance"]])

#Class averages
subject_average = df[["Math", "English", "Science"]].mean()
print("\n---Subject Averages: ")
print(subject_average)


#Visualization
#Graph 1: Student Averages
df.sort_values(by="Average").plot(
    x="Name",
    y="Average",
    kind="bar",
    title="Student Averages",
    legend=False
)

plt.ylabel("Average Student Performance")
plt.xlabel("Student Name")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig("average_scores.png")

#Graph 2: Subject Averages
df.set_index("Name")[["Math", "English", "Science"]].plot(
    kind="bar",
    title="Average Subject Scores"
)

plt.ylabel("Average Scores")
plt.xlabel("Subject Name")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig("subject_comparison.png")

#Performance Distribution
df["Performance"].value_counts().plot(
    kind="bar",
    title="Performance Distribution",
)

plt.xlabel("Performance levels")
plt.ylabel("Number of Students")
plt.show()
plt.savefig("performance_distribution.png")