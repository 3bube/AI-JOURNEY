import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('C:\\Users\\HP\\Desktop\\AI-JOURNEY\\practice\\Titanic-Dataset.csv')

missing = df.isnull().sum() / len(df) * 100

print(missing[missing > 0].sort_values(ascending=False))


# print(df.describe())

# print(df.to_string())