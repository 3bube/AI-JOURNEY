from numpy import random

x = random.uniform(5, 10, size=(2, 3))

# print(x)



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.uniform(size=1000)

sns.displot(x, kind='kde')

plt.show()