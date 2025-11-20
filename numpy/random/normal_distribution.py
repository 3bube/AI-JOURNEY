from numpy import random

x = random.normal(size=(2, 3))

# print(x)


from numpy import random

x = random.normal(size=(2, 3))

# print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()