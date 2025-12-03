import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

# print(df)
# print(df.loc[0])
# print(df.loc[[0, 1]])


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 


import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Downloads\\archive\\track_data_final.csv")

print(df) 