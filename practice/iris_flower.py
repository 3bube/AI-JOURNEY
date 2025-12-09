import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

#  Task 1 
print("Task 1")
print("First 5 rows of the Iris dataset:")
print(df.head())
print("Shape of the dataset:", df.shape)
print("Column names:", df.columns.tolist())
print("Summary of missing values:", df.isnull().sum())
print("Basic statistics of numerical columns:")
print(df.describe())

# Task 2
print("\nTask 2")
print("Duplicate rows in the dataset:")
print(df.duplicated().sum())
print("Dropping duplicate rows...")
df = df.drop_duplicates()
print("Ensure correct numeric data types:")
print(df.dtypes)
print("confirm species column is categorical:")
print(df['species'].dtype)

# Task 3
print("\nTask 3")

print("Histograms for each numerical feature:")
sns.histplot(df["sepal_length"])
plt.show()

sns.histplot(df["sepal_width"])
plt.show()


sns.histplot(df["petal_length"])
plt.show()

sns.histplot(df["petal_width"])
plt.show()
