from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pii=np.pi
pist_xy=np.array([30, 45, 60, 90, 120, 150, 180, 270]) * np.pi / 180
nim=np.array([6, 4, 3, 2, 3, 6, 6, 4]) # Kulman jakajat
varit=np.array(['red', 'green', 'blue', 'orange', 'purple', 'brown', 'black', 'cyan'])

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(f"Rad: {pist_xy[i]:.2f}",
             xy=(np.cos(pist_xy[i]), np.sin(pist_xy[i])), xycoords='data',
             xytext=(+30, +10), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.5"))


plt.show()
