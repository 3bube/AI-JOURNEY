from numpy import random


x = random.rayleigh(scale=2.0, size=(2, 3))

print(x)




from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


sns.displot(random.rayleigh(scale=2.0, size=1000), kind="kde")

plt.show()