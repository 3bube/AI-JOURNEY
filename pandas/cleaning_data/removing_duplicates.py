import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI-JOURNEY\\pandas\\cleaning_data\\data.csv")

df.drop_duplicates(inplace = True)

print(df.duplicated())