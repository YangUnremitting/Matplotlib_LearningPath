import matplotlib.pyplot as plt
import numpy as np

#################
# A simple plot #
#################
fig1, ax  = plt.subplots()               # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])     # Plot some data on the axes.
plt.show()                              # Show figure on the screen.

##########################################################
# The object-oriented interface and the pyplot interface #
##########################################################

x = np.linspace(0, 2, 100)
fig2, ax = plt.subplots()
ax.plot(x, x, label = "linear")
ax.plot(x, x**2, label="quadratic")
ax.plot(x, x**3, label="cubic")

ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_title("Simple Plot")

ax.legend()
plt.show()