import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df  = pd.read_csv("C:\\Users\\HP\\Desktop\\AI-JOURNEY\\practice\\NetFlix.csv")


# print(df.head())
# df.info()
df = df.dropna()
