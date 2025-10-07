import matplotlib.pyplot as plt
import numpy as np
import barrierlib as bl

fig = plt.figure()
ax = fig.add_subplot(111)

Barrier1 = bl.cube(1,3,10)
ax = Barrier1.draw(ax)
Barrier2 = bl.triangle(5,3,5)
ax = Barrier2.draw(ax)

plt.xlim(0,15)
plt.ylim(0,15)
plt.show()
