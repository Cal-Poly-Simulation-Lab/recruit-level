# Step 1: import matplotlib and numpy
import matplotlib.pyplot as plt
import ...

# Step 2: generate data
x = np.linspace(0, 10,100)
y = 4 + 2* np.sin(2 * x)

# Step 3:  Plot the data
fig, az = ...

ax.plot(..., ..., linewidth = 2.0)

ax.set(xlim(0,8), xticks=np.arrange(1,8),
       ylim(..., ...), yticks=...)

# Step 4: Show the plot
plt.