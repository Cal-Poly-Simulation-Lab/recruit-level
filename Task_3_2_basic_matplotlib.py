# Step 1: import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# Step 2: generate data
x = np.linspace(0, 10,100)
y = 4 + 2* np.sin(2 * x)

# Step 3:  Plot the data
fig, ax = plt.subplots()

ax.plot(x, y, linewidth = 2.0)

ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0, 8), yticks=np.arange(1,8))

# Step 4: Show the plot
plt.show()
