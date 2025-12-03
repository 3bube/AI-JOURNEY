import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Downloads\\data.csv")

new_df = df.dropna()

print(new_df.to_string())


# in place argument

import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Downloads\\data.csv")

new_df = df.dropna(inplace=True)

print(df.to_string())


# replacing empty cells with a value
import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Downloads\\data.csv")

df.fillna({"Calories": 130}, inplace=True)


# replace using mean, median, mode
import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Downloads\\data.csv")

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)


# median
import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Downloads\\data.csv")

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)


# mode

import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Downloads\\data.csv")

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)