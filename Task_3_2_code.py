# Step 1: import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# Step 2: generate data
# x is 100 envenly spaced points in the range [0, 10]
x = np.linspace(0, 10,100)
# y = 4 + sin(2 * x) - use numpy
y = 4 + 2* np.sin(2 * x)

# Step 3:  Plot the data
# create a figure and axes using suplot
fig, ax = plt.subplots()

# plot the data on the axes, use a line width of 2.0
ax.plot(x, y, linewidth = 2.0)

# set the x- and y-limits to [0, 8]
# and the x- and x-tick marks between 0 and 8 in intervals of 2
ax.set(xlim=(0, 8), xticks=np.arange(0,9,2),
       ylim=(0, 8), yticks=np.arange(0,9,2))

# Step 4: Show the plot
plt.show()
