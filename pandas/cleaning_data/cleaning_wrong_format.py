import pandas as pd


df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI-JOURNEY\\pandas\\cleaning_data\\data.csv", index_col=0)


df["Date"] = pd.to_datetime(df["Date"], format="mixed")

df.dropna(subset=["Date"], inplace=True)


print(df.to_string())


