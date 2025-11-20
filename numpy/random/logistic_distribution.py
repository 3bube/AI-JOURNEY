from numpy import random

x = random.logistic(loc = 1, scale = 2, size=(2, 3))

# print(x)



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


sns.displot(random.logistic(size= 1000), kind="kde")

# plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Logistic function definition
def logistic(x, L=1, k=1, x0=0):
    return L / (1 + np.exp(-k * (x - x0)))

# Parameters
L = 10    # Maximum value (carrying capacity)
k = 1     # Growth rate
x0 = 5    # Midpoint (where growth is fastest)

x = np.linspace(0, 10, 100)
y = logistic(x, L, k, x0)

plt.plot(x, y)
plt.title("Logistic Growth Curve (S-curve)")
plt.xlabel("Time")
plt.ylabel("Population / Value")
plt.grid(True)
plt.show()