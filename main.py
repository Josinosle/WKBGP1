import matplotlib.pyplot as plt
import barrierlib as bl
import wkblib as wkb

fig = plt.figure()
ax = fig.add_subplot(111)

Barrier1 = bl.cube(1,1,10)
ax = Barrier1.draw(ax)
Barrier2 = bl.triangle(5,1,6)
ax = Barrier2.draw(ax)
ax.set_ylim(0,1)

wavefunction = wkb.Wavefunction(10,
                                5,
                                1,
                                (Barrier1,Barrier2))
ax = wavefunction.plot(ax,0,10)


plt.show()
