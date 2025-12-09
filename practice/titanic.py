import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('C:\\Users\\HP\\Desktop\\AI-JOURNEY\\practice\\Titanic-Dataset.csv')

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop(columns=["Cabin", "PassengerId", "Name", "Ticket"])



# sns.countplot(x='Survived', data=df)
# plt.title('Survival Count')
# # plt.show()


# fig, ax = plt.subplots()
# sns.countplot(data=df, x='Sex', hue='Survived', ax=ax)

# Add value labels on each bar
# for container in ax.containers:
#     ax.bar_label(container)

# ax.set_title('Survival Count by Sex')
# ax.set_xlabel('Sex')
# ax.set_ylabel('Count')
# plt.show()


sns.histplot(df['Age'], bins=30)
plt.title('Age Distribution')
# plt.show()


sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival Count by Passenger Class')
plt.show()