import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI-JOURNEY\\pandas\\correlations\\data.csv")

# df.plot()

# plt.show()


# scatter plot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI-JOURNEY\\pandas\\correlations\\data.csv")

# df.plot(kind='scatter', x='Duration', y='Calories')
# plt.show()


# scatter plot for duration and max pulse
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI-JOURNEY\\pandas\\correlations\\data.csv")

# df.plot(kind='scatter', x='Duration', y='Maxpulse')

# plt.show()


# histogram
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI-JOURNEY\\pandas\\correlations\\data.csv")

df["Duration"].plot(kind='hist')

plt.show()